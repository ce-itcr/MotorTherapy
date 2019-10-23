using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Experimental.GlobalIllumination;
using UnityEngine.UI;
using Random = UnityEngine.Random;

public class TimerCountdown : MonoBehaviour
{
    public Text textTime;
    public float timeLeft;
    public float sphereTime;
    public Transform sphere;
    public float scaleSize;
    public float y;
    public float x;
    // Start is called before the first frame update
    void Start()
    {
        timeLeft = 60.0f;
        scaleSize = 1.15f;
        sphereTime = 5.0f;
    }

    // Update is called once per frame
    void Update()
    {
        timeLeft -= Time.deltaTime;
        scaleSize = sphere.localScale.x;
        scaleSize -= (float) (0.95/sphereTime) * Time.deltaTime;
        textTime.text = "Time: " + timeLeft.ToString("0");
        sphere.localScale = new Vector3(scaleSize,scaleSize,scaleSize);
        
        if (scaleSize <= 0.15)
        {
            scaleSize = 1.15f;
            sphere.localScale = new Vector3(scaleSize,scaleSize,scaleSize);
            sphere.localPosition = new Vector3(Random.Range(-3.6f, 3.6f),Random.Range(0.68f,4.35f),-3.05f);
        }
        if(timeLeft <= 0){
            timeLeft = 60.0f;
        }
        
    }
}
