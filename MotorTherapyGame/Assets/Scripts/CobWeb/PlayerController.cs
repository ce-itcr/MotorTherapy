using System;
using UnityEngine;
using UnityEngine.AI;
using UnityStandardAssets.Characters.ThirdPerson;

namespace CobWeb
{
    public class PlayerController : MonoBehaviour
    {
        
        public Camera cam;
        public NavMeshAgent agent;
        public Material goal;
        public ThirdPersonCharacter character;
        public float rotationSpeed;
        public float moveSpeed;
        private static bool _moving;
        private static bool _rotatingR;
        private static bool _rotatingL;
        private Rigidbody _rb;
        private bool _onLine;

        private void Start()
        {
            _rb = GetComponent<Rigidbody>();
        }

        private void Update()
        {
            var manager = KinectManager.Instance;
            if (manager == null || !manager.IsUserDetected()) return;
            var userId = manager.GetUser(0);
            
            _rotatingL = manager.GetGestureProgress(userId, KinectGestures.Gestures.RaiseLeftHand) > 0;
            _rotatingR = manager.GetGestureProgress(userId, KinectGestures.Gestures.RaiseRightHand) > 0;

            _moving = manager.GetGestureProgress(userId, KinectGestures.Gestures.RaiseLeftFoot) > 0 ||
                      manager.GetGestureProgress(userId, KinectGestures.Gestures.RaiseRightFoot) > 0;
            
            
            manager.ResetGestureListeners();
        }

        // Update is called once per frame
        private void FixedUpdate()
        {
            // Move Commands
            if (Input.GetKey(KeyCode.A) || _rotatingL) RotateLeft();
            if (Input.GetKey(KeyCode.D) || _rotatingR) RotateRight();
            if (Input.GetKey(KeyCode.W) || _moving) Move(Vector3.forward);
            else character.Move(Vector3.zero, false, false);
        }

        private void RotateRight()
        {
            var angle = rotationSpeed * Time.fixedDeltaTime;
            transform.Rotate(0, angle, 0);
            //character.Move(Vector3.right, false, false);
        }

        private void RotateLeft()
        {
            var angle = -rotationSpeed * Time.fixedDeltaTime;
            transform.Rotate(0, angle , 0);
            //character.Move(Vector3.left, false, false);

        }
        
        private void Move(Vector3 dir)
        {
            var movement = transform.rotation * dir;
            var poss = _rb.position + (Time.fixedDeltaTime * moveSpeed * movement);
            _rb.MovePosition(poss);
            character.Move(movement, false, false);
        }

        /**
        private void OnCollisionEnter(Collision other)
        {
            if (other.gameObject.tag.Equals("lines")) _onLine = true;
        }

        private void OnCollisionExit(Collision collision)
        {
            if (!collision.gameObject.tag.Equals("lines") || _onLine)
            {
                _onLine = false;
                return;
            } 

            Debug.Log("Collision");
            // Connects to Server
            var message = JsonUtility.ToJson(new Game("cobWeb", "error"));
            _client.Message(message);

            _audio.clip = missSound;
            _audio.Play();
        }**/
    }
}
