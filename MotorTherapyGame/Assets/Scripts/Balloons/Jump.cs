using System;
using UnityEngine;

namespace Balloons
{
    public class Jump : MonoBehaviour {

        public Rigidbody rb;
        public GameObject balloons;
        private Client.Client _client;
        private Game _game;
        private bool _inFloor;

        private void Awake()
        {
            _client = Client.Client.GetInstance();
        }
        
        private void OnMouseDown()
        {
            Hit();
            balloons.SendMessage("AddScore");
        }

        private void Hit()
        {
            #region Client call for data
            var message = JsonUtility.ToJson(new Game("balloons", "ok"));
            var response = _client.Message(message);
            _game = Game.CreateFromJson(response);
            #endregion
            
            const int force = 1000;
            var gameBalloons = _game.balloons;
            var x = (gameBalloons.x - 5) * Time.deltaTime * force;
            var y = gameBalloons.y * Time.deltaTime * force * 1.3f;
        
            rb.AddForce(x, y, 0);
        }
        
        private void OnCollisionEnter(Collision collision) {
            
            // Hits the floor
            if (!collision.gameObject.tag.Equals("Floor") || _inFloor) return;
            _inFloor = true;
            var message = JsonUtility.ToJson(new Game("balloons", "error"));
            _client.Message(message);
        }

        private void OnCollisionExit(Collision other)
        {
            if (other.gameObject.tag.Equals("Floor")) _inFloor = false;
        }
    }
}
