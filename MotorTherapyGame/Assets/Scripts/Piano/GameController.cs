using System;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

namespace Piano
{
    public class GameController : MonoBehaviour
    {
        public GameObject noteSpawner;
        public Text hitText;
        public Text missText;
        private Client.Client _client;
        private Game _game;
        private Spawner _spawner;

        private void Start()
        {
            _client = Client.Client.GetInstance();
            _spawner = noteSpawner.GetComponent<Spawner>();
        }

        private void Update()
        {
            if (!_spawner.Finished) return;
            var message = JsonUtility.ToJson(new Game("piano", "ok"));
            var response = _client.Message(message);
            _game = Game.CreateFromJson(response);
            if (_game != null) _spawner.Spawn(_game.piano.colors, _game.piano.points, _game.piano.time);
            if (_game.status == "end")
            {
             Results();   
            }

        }

        public void AddHitScore() => hitText.SendMessage("AddScore");

        public void AddMissScore() => missText.SendMessage("AddScore");
    
        // Returns to the previous Scene
        public void Back()
        {
            SceneManager.LoadScene("AppInterface");
        }

        public void Results()
        {
            SceneManager.LoadScene("Results");
        }
        
    }
}
