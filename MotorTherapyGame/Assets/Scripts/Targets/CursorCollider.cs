using System;
using System.Collections;
using System.Collections.Generic;
using Piano;
using UnityEngine;
using UnityEngine.UI;
using Object = System.Object;

public class CursorCollider : MonoBehaviour
{

    public GameObject targets;
    public Transform cursor;
    public Rigidbody rb;
    public bool _onCollision;
    public float time;
    
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        rb.MovePosition(new Vector3(cursor.position.x*5, cursor.position.y*5,-3.05f));
    }

    private void OnCollisionEnter(Collision other)
    {
        if (other.gameObject.tag == "target" && ((Time.time - time) > 2) && !_onCollision)
        {
            _onCollision = true;
            time = Time.time; 
            targets.SendMessage("Hit");
        }
    }
    
    private void OnCollisionExit(Collision other)
    {
        if (other.gameObject.tag.Equals("target")) _onCollision = false;
    }
}
