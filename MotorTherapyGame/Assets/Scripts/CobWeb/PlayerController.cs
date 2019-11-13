using System;
using UnityEngine;
using UnityEngine.AI;

namespace CobWeb
{
    public class PlayerController : MonoBehaviour
    {
        public Camera cam;
        public NavMeshAgent agent;
        public Material goal;
        public float rotationSpeed = 50f;
        public float moveSpeed = 10f;
        private Rigidbody _rb;

        private void Start()
        {
            _rb = GetComponent<Rigidbody>();
        }

        // Update is called once per frame
        private void FixedUpdate()
        {
            if (Input.GetMouseButtonDown(0))
            {
                Ray ray = cam.ScreenPointToRay(Input.mousePosition);
                RaycastHit hit;
            
                if (Physics.Raycast(ray, out hit))
                {
                    agent.SetDestination(hit.point);
                }
            }
        
            // Move Commands
            if (Input.GetKey(KeyCode.A)) RotateLeft();
            if (Input.GetKey(KeyCode.D)) RotateRight();
            if (Input.GetKey(KeyCode.W)) MoveForward();
        }

        private void RotateRight()
        {
            var angle = rotationSpeed * Time.fixedDeltaTime;
            transform.Rotate(0, angle, 0);
        }

        private void RotateLeft()
        {
            var angle = -rotationSpeed * Time.fixedDeltaTime;
            transform.Rotate(0, angle , 0);
        }

        private void MoveForward()
        {
            var movement = transform.rotation * Vector3.forward;
            var poss = _rb.position + (Time.fixedDeltaTime * moveSpeed * movement);
            _rb.MovePosition(poss);
        }
    }
}
