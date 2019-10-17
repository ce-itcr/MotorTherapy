<<<<<<< HEAD
﻿using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Score : MonoBehaviour
{

    public Text scoreText;
    public string tag = "";
    private int _score = 0;
    
    // Update is called once per frame
    private void Update()
    {
        scoreText.text = $"{tag} : {_score.ToString()}";
    }

    public void AddScore() => _score += 1;
=======
﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Experimental.GlobalIllumination;
using UnityEngine.SocialPlatforms.Impl;
using UnityEngine.UI;
using UnityEngine.XR.WSA.WebCam;

public class Score : MonoBehaviour{

    public static Score instance { get; private set; }
    public void Awake() {
        if (instance == null) {
            instance = this;
            DontDestroyOnLoad(gameObject);
        } else {
            Destroy(gameObject);
        }
    }
    public Text scoreText;
    public int score;
    // Start is called before the first frame update
    void Start() {
        score = 0;
    }

    // Update is called once per frame
    private void Update() {
        scoreText.text = "Score: " + score;
    }
>>>>>>> feature-balloons
}
