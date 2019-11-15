using System;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using UnityEngine.SceneManagement;

namespace CobWeb
{
    public class CobWeb : MonoBehaviour
    {
        private Client.Client _client;
        private LineRenderer lineRenderer;
        private Game _game;
        public GameObject target;
        public Material wall;
        public GameObject ground;
        private float _height;
        private float _width;
        private List<List<GameObject>> _matrix = new List<List<GameObject>>();
        
        public Color c1 = Color.yellow;
        public Color c2 = Color.red;
        private LineRenderer line;

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

            lineRenderer = gameObject.AddComponent<LineRenderer>();
            lineRenderer.material = wall;
            lineRenderer.widthMultiplier = 0.6f;
            lineRenderer.positionCount = 200;

            float alpha = 1.0f;
            Gradient gradient = new Gradient();
            gradient.SetKeys(
                new GradientColorKey[] { new GradientColorKey(c1, 0.0f), new GradientColorKey(c2, 1.0f) },
                new GradientAlphaKey[] { new GradientAlphaKey(alpha, 0.0f), new GradientAlphaKey(alpha, 1.0f) }
            );
            lineRenderer.colorGradient = gradient;
            
            InstantiatedTargets();
            //CreatePaths();
        }


        private void Update()
        {
            int rows = _matrix[0].Count;
            int columns = _matrix.Count;
            int counter = 0;
            for (int i = 0; i < columns; i++)
            {
                for (int j = 0; j < rows; j++)
                {
                    Vector3 pos1 = _matrix[i][j].transform.position;
                    if (i == (columns - 1) && j == (rows - 1))
                    {

                    }
                    else if (j == rows - 1)
                    {

                    }
                    else if (i == columns - 1)
                    {

                    }
                    else
                    {
                        Vector3 pos2 = _matrix[i][j + 1].transform.position;
                        Vector3 pos3 = _matrix[i + 1][j].transform.position;
                        lineRenderer.SetPosition(counter, pos1);
                        counter++;
                        lineRenderer.SetPosition(counter, pos2);
                        counter++;
                        lineRenderer.SetPosition(counter, pos3);
                        counter++;
                    }
                }
            }

        }

        private void InstantiatedTargets()
        {
            var rows = 8;
            var columns = 8;
            var xOffset = _width / (rows + 1);
            var zOffset = _height / (columns + 1);
            var xInitial = _width / 2 + xOffset / 4;
            var zInitial = _height / 2;
            Material material = null;

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
                    var obj = Instantiate(target, new Vector3(x, 0, z), Quaternion.identity);
                    row.Add(obj);
                }
                _matrix.Add(row);
            }
        }

        private void CreatePaths()
        {
            // Reads the matrix and generates the connections
            
            int rows = _matrix[0].Count;
            int columns = _matrix.Count;

            for (int i = 0; i < columns; i++)
            {
                for (int j = 0; j < rows; j++)
                {
                    Vector3 pos1 = _matrix[i][j].transform.position;
                    if (i == (columns - 1) && j == (rows - 1))
                    {

                    }
                    else if (j == rows - 1)
                    {

                    }
                    else if (i == columns - 1)
                    {

                    }
                    else
                    {
                        Vector3 pos2 = _matrix[i][j + 1].transform.position;
                        Vector3 pos3 = _matrix[i + 1][j].transform.position;
                        //double distance12 = Vector3.Distance(pos1, pos2);
                        //double distance13 = Vector3.Distance(pos1, pos3);
                        //Vector3 v2 = (pos2 - pos1).normalized;
                        //Instantiate(line, new Vector3(0,0,0), Quaternion.identity);
                        //line.SetPosition(0, pos1);
                        //line.SetPosition(1, pos2);
                    }
                }
            }
        }
        
    }
}
    
