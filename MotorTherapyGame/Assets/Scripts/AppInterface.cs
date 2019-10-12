﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AppInterface : MonoBehaviour
{
        
    [SerializeField] private GameObject HomeCanvas = null;
    [SerializeField] private GameObject InfoCanvas = null;
    [SerializeField] private GameObject SettingsCanvas = null;
    
    // Start is called before the first frame update
    void Start()
    {
        ShowHomeCanvas();
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    
    public void ShowHomeCanvas()
    {
        HomeCanvas.SetActive(true);
        InfoCanvas.SetActive(false);
        SettingsCanvas.SetActive(false);
    }

    public void ShowInfoCanvas()
    {
        HomeCanvas.SetActive(false);
        InfoCanvas.SetActive(true);
        SettingsCanvas.SetActive(false);
    }
    
    public void ShowSettingsCanvas()
    {
        HomeCanvas.SetActive(false);
        InfoCanvas.SetActive(false);
        SettingsCanvas.SetActive(true);
    }
}
