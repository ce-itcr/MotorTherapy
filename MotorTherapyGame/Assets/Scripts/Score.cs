using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Score : MonoBehaviour
{

    public Text scoreText;
    public string tag = "";
    private int score = 0;
    
    // Update is called once per frame
    private void Update()
    {
        scoreText.text = $"{tag} : {score.ToString()}";
    }

    public void AddScore() => score += 1;
}
