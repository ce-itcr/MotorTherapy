using UnityEngine;

namespace Piano
{
    public class PianoFlag : MonoBehaviour
    {
        public GameObject gameController;
        public AudioClip hitSound;
        public AudioClip missSound;
        private bool _noteCollision = false;
        private GameObject _noteCollider;
        private AudioSource _audio;

        private void Start()
        {
            _audio = GetComponent<AudioSource>();
        
        }

        public void Hit()
        {
            if (_noteCollision && _noteCollider.tag.Equals("Note"))
            {
                var points = _noteCollider.GetComponent<Note>().points;
                AddScore(points);
                Destroy(_noteCollider);
            }
            else Miss();
        }

        private void OnMouseDown()
        {
            if (_noteCollision && _noteCollider.tag.Equals("Note"))
            {
                var points = _noteCollider.GetComponent<Note>().points;
                AddScore(points);
                Destroy(_noteCollider);
            }
            else Miss();
        }

        private void OnCollisionEnter(Collision other)
        {
            _noteCollision = true;
            _noteCollider = other.collider.gameObject;
        }

        private void OnCollisionExit()
        {
            if (_noteCollider.tag.Equals("Note"))
            {
                _noteCollision = false;
                Destroy(_noteCollider);
                _noteCollider = null;
                Miss();
            }
        }
    
        private void AddScore(int points)
        {
            Debug.Log("HIT");
            gameController.SendMessage("AddHitScore", points);
            _audio.clip = hitSound;
            _audio.Play();
        }

        private void Miss()
        {
            Debug.Log("MISS");
            gameController.SendMessage("AddMissScore");
            _audio.clip = missSound;
            _audio.Play();
        }
    }
}
