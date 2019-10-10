using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PianoFlag : MonoBehaviour
{
    private bool _noteCollision = false;

    private void OnMouseDown()
    {
        if (_noteCollision) Hit();
        else Miss();
    }

    private void OnCollisionEnter() => _noteCollision = true;

    private void OnCollisionExit() => _noteCollision = false;

    private void Hit()
    {
        Debug.Log("HIT");
    }

    private void Miss()
    {
        Debug.Log("MISS");
    }
}
