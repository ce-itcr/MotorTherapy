using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

namespace Balloons
{
    public class BalloonsController : MonoBehaviour
    {
        public Text score;
        private int _points;
        private Game _game;
        
        // Returns to the previous Scene
        public void Back()
        {
            SceneManager.LoadScene("AppInterface");
        }
        
        private void Update()
        {
            if (_game.status == "end")
            {
                Results();   
            }
        }
        

        public void AddScore()
        {
            _points++;
            score.text = $"Score: {_points.ToString()}";
        }

        public void Hit()
        {
            AddScore();
        }
        
        public void Results()
        {
            SceneManager.LoadScene("Results");
        }
        
    }
}

