using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace CobWeb
{
    public class Map : MonoBehaviour
    {

        private Client.Client _client;
        public AudioClip missSound;
        private AudioSource _audio;
        private static bool _onLine;
        private static List<GameObject> _lines = new List<GameObject>();
        private static bool _outside;

        private void Start()
        {
            _client = Client.Client.GetInstance();
            _audio = GetComponent<AudioSource>();
        }

        private void OnCollisionEnter(Collision other)
        {
            if (other.gameObject.CompareTag("Player")) 
                _lines.Add(gameObject);
        }

        private void OnCollisionExit(Collision other)
        {
            if (other.gameObject.CompareTag("Player"))
                _lines.Remove(gameObject);
        }

        private void Update()
        {
            if (_lines.Count == 0 && !_outside) NotOnLine();
            if (_lines.Count > 0) _outside = false;
        }

        private void NotOnLine()
        {
            _outside = true;
            
            // Connects to Server
            var message = JsonUtility.ToJson(new Game("cobWeb", "error"));
            //_client.Message(message);

            _audio.clip = missSound;
            _audio.Play();
        }
    }
}
