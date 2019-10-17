using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SocialPlatforms.Impl;
using UnityEngine.UI;
using UnityEngine.XR.WSA.WebCam;

public class SphereCollision : MonoBehaviour
{
    public Camera cam;
    public Transform sphere;
    public Text scoreText;
    public int score;
    // Start is called before the first frame update
    void Start()
    {
        score = 0;
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetMouseButtonDown(0)) {
            Ray ray = cam.ScreenPointToRay(Input.mousePosition);
            RaycastHit hit;
            if(Physics.Raycast(ray, out hit)) {
                sphere.localScale = new Vector3(1.15f,1.15f,1.15f);
                sphere.localPosition = new Vector3(Random.Range(-3.6f, 3.6f),Random.Range(0.68f,4.35f));
                scoreText.text =  "Score: " + ++score;
            }
        }
        
    }
}
