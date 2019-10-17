using UnityEngine;

public class Jump : MonoBehaviour {

    public Rigidbody rb;

    // Start is called before the first frame update
    void Start() {

    }

    // Update is called once per frame
    void Update() {
        
    }

    private void OnCollisionEnter(Collision collision) {
        rb.velocity = Vector3.zero;
        if (Random.value > 0.5f)
        {
            rb.AddForce(1000 * Time.deltaTime, 20000 * Time.deltaTime, 0);
        }
        else
            rb.AddForce(-1000 * Time.deltaTime, 20000 * Time.deltaTime, 0);
    }

    public void OnMouseDown() {
        rb.velocity = Vector3.zero;
        if (Random.value > 0.5f)
        {
            rb.AddForce(1000 * Time.deltaTime, 5000 * Time.deltaTime, 0);
        }
        else
            rb.AddForce(-1000 * Time.deltaTime, 5000 * Time.deltaTime, 0);
    }
}
