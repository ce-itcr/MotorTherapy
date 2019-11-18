using System;
using System.Collections.Generic;
using System.Linq;
using TMPro;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;
using Object = System.Object;

namespace CobWeb
{
    public class CobWeb : MonoBehaviour
    {
        private Client.Client _client;
        private Game _game;
        public GameObject goal;
        public GameObject wall;
        public GameObject ground;
        public GameObject map;
        public Text time;
        public Text score;
        private int _score;
        private const float TimeMax = 60f;
        private float _startTime;
        private float _height;
        private float _width;
        private List<List<GameObject>> _matrix = new List<List<GameObject>>();
        

        // Returns to the previous Scene
        public void Back()
        {
            SceneManager.UnloadSceneAsync("Scenes/CobWeb");
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
            if (_game.status.Equals("end")) Back();
            
            // Gets Ground scale
            var scale = ground.GetComponent<MeshRenderer>().bounds.size;
            _height = scale.z;
            _width = scale.x;
            
            // Loads Matrix
            if (_game.cobWeb.cards == null) return;
            InstantiatedTargets();
            CreatePaths();

            _startTime = Time.time;
        }

        private void Update()
        {
            var t = TimeMax - (Time.time - _startTime);
            time.text = $"Time: {t:0}";
        }

        public void AddScore(int points)
        {
            _score += points;
            score.text = $"Score: {_score}";
        }

        private void LoadCard(GameObject obj, int i, int j)
        {
            var card = _game.GetCard(i, j);
            var sGoal = obj.GetComponent<Goal>();
            sGoal.word = card.name;
            sGoal.points = card.points;
            sGoal.i = i;
            sGoal.j = j;
        }

        private void InstantiatedTargets()
        {
            var rows = _game.cobWeb.rows;
            var columns = _game.cobWeb.columns;
            var xOffset = _width / (rows + 1);
            var zOffset = _height / (columns + 1);
            var xInitial = _width / 2 + xOffset / 4 - 25;
            var zInitial = _height / 2 - 25;

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
                    var obj = Instantiate(goal, new Vector3(x, 1, z), Quaternion.identity);
                    LoadCard(obj, i, j);
                    row.Add(obj);
                }
                _matrix.Add(row);
            }
        }

        private void CreatePaths()
        {
            var rows = _matrix[0].Count;
            var columns = _matrix.Count;
            for (var i = 0; i < columns; i++)
            {
                for (var j = 0; j < rows; j++)
                {
                    var pos1 = _matrix[i][j].transform.position;
                    pos1.y -= 1.4f;
                    if (i == (columns - 1) && j == (rows - 1))
                    {
                        continue;
                    }
                    else if (j == rows - 1)
                    {
                        Vector3 pos3 = _matrix[i + 1][j].transform.position;
                        pos3.y -= 1.4f;
                        
                        //wallObj.transform.localScale = new Vector3(1,0.1f,Vector3.Distance(pos1, pos2));

                        var negative = 1;
                        if (i % 2 != 0) negative = -1;
                        
                        Vector3 med1 = Vector3.Lerp(pos1, pos3, 0.5f);
                        var wallObj1 = Instantiate(wall, med1, Quaternion.identity);
                        var rotate = Vector3.Angle(pos1, pos3);
                        wallObj1.transform.Rotate(0, rotate * negative, 0);

                        var scale1 = Vector3.forward * Vector3.Distance(pos1, pos3);
                        scale1.x = 2;
                        scale1.y = 1;
                        
                        wallObj1.transform.localScale = scale1;
                        
                        wallObj1.transform.SetParent(map.transform);
                    }
                    else if (i == columns - 1)
                    {
                        Vector3 pos2 = _matrix[i][j + 1].transform.position;
                        pos2.y -= 1.4f;

                        Vector3 med = Vector3.Lerp(pos1, pos2, 0.5f);
                        var wallObj = Instantiate(wall, med, Quaternion.identity);
                        //wallObj.transform.localScale = new Vector3(1,0.1f,Vector3.Distance(pos1, pos2));

                        Vector3 scale = new Vector3(Math.Abs(pos1.x - pos2.x), Math.Abs(pos1.y - pos2.y) + 1, Math.Abs(pos1.z - pos2.z) + 2);
                        wallObj.transform.localScale = scale;

                        var negative = 1;
                        if (i % 2 != 0) negative = -1;
                        
                        wallObj.transform.SetParent(map.transform);
                    }
                    else
                    {
                        Vector3 pos2 = _matrix[i][j + 1].transform.position;
                        pos2.y -= 1.4f;
                        Vector3 pos3 = _matrix[i + 1][j].transform.position;
                        pos3.y -= 1.4f;
                        /*lineRenderer.SetPosition(counter, pos1);
                        counter++;
                        lineRenderer.SetPosition(counter, pos2);
                        counter++;
                        lineRenderer.SetPosition(counter, pos3);
                        counter++;*/

                        Vector3 med = Vector3.Lerp(pos1, pos2, 0.5f);
                        var wallObj = Instantiate(wall, med, Quaternion.identity);
                        //wallObj.transform.localScale = new Vector3(1,0.1f,Vector3.Distance(pos1, pos2));

                        Vector3 scale = new Vector3(Math.Abs(pos1.x - pos2.x), Math.Abs(pos1.y - pos2.y) + 1, Math.Abs(pos1.z - pos2.z) + 2);
                        wallObj.transform.localScale = scale;

                        var negative = 1;
                        if (i % 2 != 0) negative = -1;
                        
                        Vector3 med1 = Vector3.Lerp(pos1, pos3, 0.5f);
                        var wallObj1 = Instantiate(wall, med1, Quaternion.identity);
                        var rotate = Vector3.Angle(pos1, pos3);
                        wallObj1.transform.Rotate(0, rotate * negative, 0);

                        var scale1 = Vector3.forward * Vector3.Distance(pos1, pos3);
                        scale1.x = 2;
                        scale1.y = 1;
                        
                        wallObj1.transform.localScale = scale1;

                        
                        wallObj.transform.SetParent(map.transform);
                        wallObj1.transform.SetParent(map.transform);
                    }
                }
            }

        }
    }
}
    
