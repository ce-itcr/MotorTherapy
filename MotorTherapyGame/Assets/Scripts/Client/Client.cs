using System;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using UnityEngine;

namespace Client
{
    public class Client : MonoBehaviour
    {
        private TcpClient _socket;
        private Thread _thread;
        private const string Ip = "127.0.0.1";
        private const int Port = 8888;

        private void Start()
        {
            Connect();
        }

        private void OnDestroy()
        {
            _socket.Close();
            _thread.Abort();
        }

        private void Connect()
        {
            try
            {
                Debug.Log("Client starting...");
                _thread = new Thread(new ThreadStart(Listen)) {IsBackground = true};
                _thread.Start();
            }
            catch (Exception  e)
            {
                Debug.LogError(e);
            }
        }

        private void Listen()
        {
            try
            {
                _socket = new TcpClient(Ip, Port);
                Debug.LogFormat("Client connected to {0}:{1}", Ip, Port);
                while (true)
                {
                    var stream = _socket.GetStream() ;
                    var serverMessage = ReadStream(stream);
                    Debug.LogFormat("Client receive: {0}", serverMessage);
                }
            }
            catch (SocketException e)
            {
                Debug.LogError(e);
            }
        }

        private string ReadStream(NetworkStream stream)
        {
            var serverMessage = "";
            var data = new byte[1024];
            int length;
            // Read incoming stream into byte array. 					
            while ((length = stream.Read(data, 0, data.Length)) != 0)
            {
                var incomingData = new byte[length];
                Array.Copy(data, 0, incomingData, 0, length);
                // Convert byte array to string message. 						
                serverMessage = Encoding.ASCII.GetString(incomingData);
            }
            return serverMessage;
        }

        private void SendMessage(string message)
        {
            if (_socket == null) return;
            try
            {			
                var stream = _socket.GetStream();
                if (!stream.CanWrite) return;
                			
                // Convert string message to byte array.
                byte[] clientMessageAsByteArray = Encoding.ASCII.GetBytes(message);
                stream.Write(clientMessageAsByteArray, 0, clientMessageAsByteArray.Length);
            }
            catch (SocketException e)
            {
                Debug.LogError(e);
            }
        }
    }
}

