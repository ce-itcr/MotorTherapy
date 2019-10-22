using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

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

    private void OnMouseDown()
    {
        if (_noteCollision)
        {
            Hit();
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
        _noteCollision = false;
        Destroy(_noteCollider);
        _noteCollider = null;
        Miss();
    }

    private void Hit()
    {
        Debug.Log("HIT");
        gameController.SendMessage("AddHitScore");
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
