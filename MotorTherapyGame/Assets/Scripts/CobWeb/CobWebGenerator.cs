using System;
using UnityEngine;

namespace CobWeb
{
    public class CobWebGenerator: MonoBehaviour
    {

        public GameObject target;
        public GameObject plane;
        public int height;
        public int width;

        private void Start()
        {
            instatiateTargets();
        }

        public void instatiateTargets()
        {
            for (int y = 0; y < height; y++)
            {
                for (int x = 0; x < width; x++)
                {
                    //Instantiate(target, new Vector3(x*plane.transform.localScale.x/height,0, y*transform.localScale.z/width), transform.rotation);
                    Instantiate(target, new Vector3(x*50/height,0, y*50/width), transform.rotation);
                }
            }
        }
    }
}