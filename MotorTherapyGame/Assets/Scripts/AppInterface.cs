using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

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

    public void OpenTargetsGame() {
        SceneManager.LoadScene("Scenes/Targets");
    }
    
    public void OpenCobWebGame() {
        SceneManager.LoadScene("Scenes/CobWeb");
    }
    
    public void OpenPianoGame() {
        SceneManager.LoadScene("Scenes/PianoScene");
    }
    
    public void OpenBalloonsGame() {
        SceneManager.LoadScene("Scenes/Balloons");
    }
}
