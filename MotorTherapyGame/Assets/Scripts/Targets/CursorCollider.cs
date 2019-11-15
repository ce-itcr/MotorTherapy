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
    private float time;
    public float zPosition;

    public int mult;
    //public GameObject balloons;
    
    // Start is called before the first frame update
    void Start()
    {
        time = 0;
        _onCollision = false;
    }

    // Update is called once per frame
    void Update()
    {
       rb.MovePosition(new Vector3(cursor.position.x * mult, cursor.position.y * mult,zPosition));
       print(cursor.position.y);
    }
    private void OnCollisionEnter(Collision other)
    {
        if (other.gameObject.tag == "target" && ((Time.time - time) > 2) && !_onCollision)
        {
            _onCollision = true;
            time = Time.time; 
            targets.SendMessage("Hit");
        }

        if (other.gameObject.tag == "flag" && ((Time.time - time) > 2) && !_onCollision)
        {
            _onCollision = true;
            time = Time.time;
            other.gameObject.SendMessage("Hit");
        }
        
        if (other.gameObject.tag == "balloon" && ((Time.time - time) > 2) && !_onCollision)
        {
            _onCollision = true;
            time = Time.time;
            targets.SendMessage("Hit");
            other.gameObject.SendMessage("Hit");
        }

    }
    
    private void OnCollisionExit(Collision other)
    {
        if (other.gameObject.tag.Equals("target")) _onCollision = false;
        if (other.gameObject.tag.Equals("flag")) _onCollision = false;
        if (other.gameObject.tag.Equals("balloon")) _onCollision = false;
    }
}