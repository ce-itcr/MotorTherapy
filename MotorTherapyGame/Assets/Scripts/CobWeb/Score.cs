using UnityEngine;
using UnityEngine.UI;

namespace CobWeb
{
    public class Score : MonoBehaviour{

        public static Score instance { get; private set; }
        public void Awake() {
            if (instance == null) {
                instance = this;
                DontDestroyOnLoad(gameObject);
            } else {
                Destroy(gameObject);
            }
        }
        public Text scoreText;
        public int score;
        // Start is called before the first frame update
        void Start() {
            score = 0;
        }

        // Update is called once per frame
        private void Update() {
            scoreText.text = "Score: " + score;
        }
    }
}