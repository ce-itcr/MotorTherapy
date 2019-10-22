using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class GameController : MonoBehaviour
{

    public Text hitText;
    public Text missText;
    
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void AddHitScore() => hitText.SendMessage("AddScore");

    public void AddMissScore() => missText.SendMessage("AddScore");
}
