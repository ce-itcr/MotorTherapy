using System;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

namespace CobWeb
{
    public class CobWeb : MonoBehaviour
    {
        private Client.Client _client;
        private Game _game;
        public GameObject target;
        public GameObject ground;
        private float _height;
        private float _width;
        private List<List<GameObject>> _matrix;


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
            // Connects to Server
            var message = JsonUtility.ToJson(new Game("cobWeb", "ok"));
            var response = _client.Message(message);
            _game = Game.CreateFromJson(response);

            // Scale of the Ground and Instantiate Targets
            var scale = ground.GetComponent<MeshRenderer>().bounds.size;
            _height = scale.z;
            _width = scale.x;
            
            InstantiatedTargets();
            CreatePaths();
        }

        private void InstantiatedTargets()
        {
            var rows = 5;
            var columns = 5;
            var xOffset = _width / (rows + 1);
            var zOffset = _height / (columns + 1);
            var xInitial = _width / 2 + xOffset / 4;
            var zInitial = _height / 2;
            
            for (var j = 0; j < rows; ++j)
            {
                var z = (j + 1) * zOffset - zInitial;
                var row = new List<GameObject>();
                for (var i = 0; i < columns; ++i)
                {
                    // Creates a gap between rows
                    var odd = 0f;
                    if (j % 2 != 0) odd = xOffset / 2;
                    
                    // Creates the Target
                    var x = (i + 1) * xOffset - xInitial + odd;
                    var obj = Instantiate(target, new Vector3(x,0, z), Quaternion.identity);
                    row.Add(obj);
                }
                _matrix.Add(row);
            }
        }

        private void CreatePaths()
        {
            // Reads the matrix nad generates the connections
        }
        
    }
}
