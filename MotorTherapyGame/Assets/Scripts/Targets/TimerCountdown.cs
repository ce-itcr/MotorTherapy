using UnityEngine;
using UnityEngine.UI;

namespace Targets
{
    public class TimerCountdown : MonoBehaviour
    {
        public GameObject gameController;
        public Text textTime;
        public float timeLeft;
        public float sphereTime;
        public Transform sphere;
        public float scaleSize;
        public float y;
        public float x;
        // Start is called before the first frame update
        void Start()
        {
            timeLeft = 60.0f;
            scaleSize = 1.15f;
            sphereTime = 5.0f;
            gameController.SendMessage("Spawn");
        }

        // Update is called once per frame
        void Update()
        {
            timeLeft -= Time.deltaTime;
            scaleSize = sphere.localScale.x;
            scaleSize -= (float) (0.95/sphereTime) * Time.deltaTime;
            textTime.text = "Time: " + timeLeft.ToString("0");
            sphere.localScale = new Vector3(scaleSize,scaleSize,scaleSize);
        
            if (scaleSize <= 0.15)
            {
                scaleSize = 1.15f;
                gameController.SendMessage("Spawn");
            }
            if(timeLeft <= 0){
                gameController.SendMessage("End");
            }
        }
    }
}
