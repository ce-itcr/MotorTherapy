using UnityEngine;

namespace Balloons
{
    public class Jump : MonoBehaviour {

        public Rigidbody rb;
        public GameObject balloons;
        private Client.Client _client;
        private Game _game;

        private void Awake()
        {
            _client = Client.Client.GetInstance();
        }
        
        private void OnMouseDown()
        {
            Hit();
            balloons.SendMessage("AddScore");
        }

        private void Hit()
        {
            #region Client call for data
            var message = JsonUtility.ToJson(new Game("balloons", "ok"));
            var response = _client.Message(message);
            _game = Game.CreateFromJson(response);
            #endregion
            
            const int force = 1000;
            var balloons = _game.balloons;
            var x = (balloons.x - 5) * Time.deltaTime * force;
            var y = balloons.y * Time.deltaTime * force * 1.3f;
        
            rb.AddForce(x, y, 0);
        }

    }
}
