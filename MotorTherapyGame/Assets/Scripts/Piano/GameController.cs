using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class GameController : MonoBehaviour
{

    public Text hitText;
    public Text missText;
    
    public void AddHitScore() => hitText.SendMessage("AddScore");

    public void AddMissScore() => missText.SendMessage("AddScore");
    
    // Returns to the previous Scene
    public void Back()
    {
        SceneManager.LoadScene("AppInterface");
    }
}
