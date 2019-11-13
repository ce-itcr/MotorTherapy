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
        public static bool Moving;
        public static bool RotatingR;
        public static bool RotatingL;
        private Rigidbody _rb;

        private void Start()
        {
            _rb = GetComponent<Rigidbody>();
        }

        // Update is called once per frame
        private void FixedUpdate()
        {
            // Move Commands
            if (Input.GetKey(KeyCode.A) || RotatingL) RotateLeft();
            if (Input.GetKey(KeyCode.D) || RotatingR) RotateRight();
            if (Input.GetKey(KeyCode.W) || Moving) Move(Vector3.forward);
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
    }
}
