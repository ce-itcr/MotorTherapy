﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class TextUpdate : MonoBehaviour
{
    public GUIText gText;
    
    // Update is called once per frame
    void Update()
    {
        GetComponent<Text>().text = gText.text;
    }
}
