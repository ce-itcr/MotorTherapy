using UnityEngine;

namespace CobWeb
{
    public class PopulateGrid : MonoBehaviour
    {

        public GameObject prefab;
        public int numberToCreate;
    
        // Start is called before the first frame update
        void Start()
        {
            Populate();
        }

        // Update is called once per frame
        void Update()
        {
        
        }

        void Populate()
        {
            GameObject newObj;
        
            for (int i=0; i<numberToCreate; i++)
            {
                newObj = (GameObject) Instantiate(prefab, transform);
                // newObj.GetComponent().color = Random.ColorHSV();
            }
        }
    
    }
}
