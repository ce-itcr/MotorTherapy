using UnityEditor;
using UnityEngine;
using UnityEngine.Experimental.UIElements;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

namespace Targets
{
    public class SphereCollision : MonoBehaviour
    {
        private GameController gameController;
        public Camera cam;
        public Text scoreText;
        public int score;
        public Transform handCursor;

        // Start is called before the first frame update
        void Start()
        {
            score = 0;
            gameController = GetComponent<GameController>();
        }

        // Update is called once per frame
        void Update()
        {
            if (Input.GetMouseButtonDown(0)) {
                Ray ray = cam.ScreenPointToRay(Input.mousePosition);
                RaycastHit hit;
                if(Physics.Raycast(ray, out hit)) {
                    // if collision
                    Hit();
                }
            }
        }

        public void Hit()
        {
            gameController.SendMessage("Spawn");
            scoreText.text =  "Score: " + ++score;
        }

        public void OpenAppInterface()
        {
            SceneManager.LoadScene("AppInterface");
        }
    }
}
