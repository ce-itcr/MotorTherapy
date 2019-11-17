using UnityEngine;

namespace Piano
{
    public class Note : MonoBehaviour
    {
        public Rigidbody rb;
        public int points;
        private const float YSpeed = -0.05f;

        private void Update()
        {
            Move();
        }

        private void Move()
        {
            var poss = transform.position;
            poss.y += YSpeed;
            rb.MovePosition(poss);
        }
    }
}
