using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Note : MonoBehaviour
{
    public Rigidbody rb;
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
