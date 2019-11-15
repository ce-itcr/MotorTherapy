using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

namespace Balloons
{
    public class BalloonsController : MonoBehaviour
    {
        public Text score;
        private int _points;
        
        // Returns to the previous Scene
        public void Back()
        {
            SceneManager.LoadScene("AppInterface");
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
    }
}

