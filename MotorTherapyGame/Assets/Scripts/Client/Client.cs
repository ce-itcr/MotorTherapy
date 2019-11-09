using System;
using System.IO;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using UnityEngine;

/**
 * @Author Jose Acuna
 * Last time edited 22/10/19 by Jose Acuna
 * @Reference https://gist.github.com/danielbierwirth/0636650b005834204cb19ef5ae6ccedb
 */
namespace Client
{
    public class Client
    {
        private static Client _instance;
        private TcpClient _socket;
        private string _ip = "192.168.1.116";
        private int _port = 8888;

        public static Client GetInstance()
        {
            return _instance ?? (_instance = new Client());
        }

        public string Message(string message)
        {
            var response = "";
                Connect();
                Send(message);
                response = Listen();
                Disconnect();
            return response;
        }
        
        private void Start()
        {
            Debug.Log("Client starting...");
        }

        private void OnDestroy()
        {
            _socket?.Close();
        }

        private void Connect()
        {
            try
            {
                _socket = new TcpClient(_ip, _port);
                Debug.LogFormat("Client connected to {0}:{1}", _ip, _port);
            }
            catch (SocketException  e)
            {
                Debug.LogError(e);
            }
        }

        private void Disconnect()
        {
            _socket.Close();
            Debug.LogFormat("Client disconnected from {0}:{1}", _ip, _port);
        }

        private string Listen()
        {
            var serverMessage = "";
            try
            {
                var stream = _socket.GetStream() ;
                serverMessage = ReadStream(stream);
                Debug.LogFormat("Client receive: {0}", serverMessage);
            }
            catch (SocketException e)
            {
                Debug.LogError(e);
            }
            return serverMessage;
        }

        private string ReadStream(NetworkStream stream)
        {
            var serverMessage = new StringBuilder();
            var buffer = new byte[256];
            
            // Incoming message may be larger than the buffer size.
            do{
                var bytes = stream.Read(buffer, 0, buffer.Length);
                serverMessage.AppendFormat("{0}", Encoding.ASCII.GetString(buffer, 0, bytes));
            }
            while(stream.DataAvailable);
            
            return serverMessage.ToString();
        }

        private void Send(string message)
        {
            if (_socket == null) return;
            try
            {			
                var stream = _socket.GetStream();
                if (!stream.CanWrite) return;
                			
                // Convert string message to byte array.
                var clientMessageAsByteArray = Encoding.ASCII.GetBytes(message);
                stream.Write(clientMessageAsByteArray, 0, clientMessageAsByteArray.Length);
                Debug.LogFormat("Client send: {0}", message);
            }
            catch (SocketException e)
            {
                Debug.LogError(e);
            }
        }

        public string Ip
        {
            get => _ip;
            set => _ip = value;
        }

        public int Port
        {
            get => _port;
            set => _port = value;
        }
    }
}

