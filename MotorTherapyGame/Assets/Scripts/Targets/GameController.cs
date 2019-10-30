using Piano;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

namespace Targets
{
    public class GameController : MonoBehaviour
    {
        public GameObject timeController;
        public Transform sphere;
        private Transform _sphereIns;
        private Client.Client _client;
        private Game _game;

        public void Spawn()
        {
            var message = JsonUtility.ToJson(new Game("targets", "ok"));
            var response = _client.Message(message);
            _game = Game.CreateFromJson(response);
            var targets = _game.targets;
            sphere = CreateSphere(targets.x, targets.y);
            var timerScript = timeController.GetComponent<TimerCountdown>();
            timerScript.sphereTime = targets.time;
            timerScript.sphere = sphere;
        }

        public void End()
        {
            
        }
        
        private void Awake()
        {
            _client = Client.Client.GetInstance();
        }

        private Transform CreateSphere(int x, int y)
        {
            if (_sphereIns != null) Destroy(_sphereIns.gameObject);
            const float xOffset = 3.4f;
            const float yOffset = 0.33f;
            var xPoss = Mathf.Clamp(x, 0, 7) - xOffset;
            var yPoss = Mathf.Clamp(y, 0, 4) - yOffset;
            var poss = new Vector3(xPoss, yPoss,-3.05f);
            _sphereIns = Instantiate(sphere, poss, sphere.transform.rotation);
            _sphereIns.localScale = new Vector3(1.15f,1.15f,1.15f);
            return _sphereIns;
        }
    }
}
