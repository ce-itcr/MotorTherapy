using System;
using UnityEngine;
using UnityEngine.SceneManagement;

namespace CobWeb
{
    public class CobWeb : MonoBehaviour
    {
        private Client.Client _client;
        private Game _game;
        public GameObject target;
        public int height;
        public int width;


        // Returns to the previous Scene
        public void Back()
        {
            SceneManager.LoadScene("AppInterface");
        }

        private void Awake()
        {
            _client = Client.Client.GetInstance();
        }

        private void Start()
        {
            var message = JsonUtility.ToJson(new Game("cobWeb", "ok"));
            var response = _client.Message(message);
            _game = Game.CreateFromJson(response);
        }

        public void instatiateTargets()
        {
            {
                for (int y = 0; y < height; ++y)
                {
                    for (int x = 0; x < width; ++x)
                    {
                        Instantiate(target, new Vector3(x, y, 0), Quaternion.identity);
                    }
                }
            }
        }
    }
}
