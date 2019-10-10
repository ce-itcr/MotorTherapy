using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PianoFlag : MonoBehaviour
{
    public AudioClip hitSound;
    public AudioClip missSound;
    private bool _noteCollision = false;
    private AudioSource _audio;

    private void Start()
    {
        _audio = GetComponent<AudioSource>();
    }

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
        _audio.clip = hitSound;
        _audio.Play();
    }

    private void Miss()
    {
        Debug.Log("MISS");
        _audio.clip = missSound;
        _audio.Play();
    }
}
