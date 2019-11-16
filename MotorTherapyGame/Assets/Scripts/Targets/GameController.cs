using System;
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

        private void Update()
        {
	        if (_game.status == "end")
	        {
		        Results();   
	        }
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
	        var poss = new Vector3(xPoss, yPoss, -3.05f);

	        // Creates the Sphere
	        _sphereIns = Instantiate(sphere, poss, sphere.transform.rotation);
	        _sphereIns.tag = "target";
	        _sphereIns.localScale = new Vector3(1.15f, 1.15f, 1.15f);

	        // Sets a random color to the sphere
	        var material = TilesColors.RandomMeshColor();
	        _sphereIns.GetComponent<MeshRenderer>().sharedMaterial = material;
	        return _sphereIns;
        }
        
        public void Results()
        {
	        SceneManager.LoadScene("Results");
        }
    }
}
