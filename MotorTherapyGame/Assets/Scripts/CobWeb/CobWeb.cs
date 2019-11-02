using UnityEngine;
using UnityEngine.SceneManagement;

public class CobWeb : MonoBehaviour
{
    // Returns to the previous Scene
    public void Back()
    {
        SceneManager.LoadScene("AppInterface");
    }
}
