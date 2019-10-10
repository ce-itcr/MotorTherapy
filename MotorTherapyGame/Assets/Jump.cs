using UnityEngine;

public class Jump : MonoBehaviour {

    public Rigidbody rb;

    // Start is called before the first frame update
    void Start() {

    }

    // Update is called once per frame
    void Update() {
        
    }

    public void OnMouseDown() {
        if (Random.value > 0.5f)
            rb.AddForce(5000 * Time.deltaTime, 30000 * Time.deltaTime, 0);
        else
            rb.AddForce(-5000 * Time.deltaTime, 30000 * Time.deltaTime, 0);
    }
}
