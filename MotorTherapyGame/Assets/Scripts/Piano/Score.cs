using UnityEngine;
using UnityEngine.UI;

namespace Piano
{
    public class Score : MonoBehaviour
    {

        public Text scoreText;
        public new string tag = "";
        private int _score = 0;

        // Update is called once per frame
        private void Update()
        {
            scoreText.text = $"{tag} : {_score.ToString()}";
        }

        public void AddScore() => _score += 1;
    }
}