using System;
using System.Collections;
using UnityEngine;

namespace CobWeb
{
    public class Map : MonoBehaviour
    {

        private Client.Client _client;
        public AudioClip missSound;
        private AudioSource _audio;
        private bool _onLine;

        private void Start()
        {
            _client = Client.Client.GetInstance();
            _audio = GetComponent<AudioSource>();
        }

        private void OnCollisionEnter(Collision other)
        {
            if (other.gameObject.CompareTag("Player")) _onLine = true;
        }

        private void OnCollisionExit(Collision other)
        {
            if (other.gameObject.CompareTag("Player"))
            {
                StartCoroutine(Collision());
            }
        }

        IEnumerator Collision()
        {
            yield return new WaitForSeconds(0.5f);
            if (_onLine)
            {
                _onLine = false;
                yield break;
            }

            Debug.Log("Collision");
            // Connects to Server
            var message = JsonUtility.ToJson(new Game("cobWeb", "error"));
            //_client.Message(message);

            _audio.clip = missSound;
            _audio.Play();
        }
    }
}
