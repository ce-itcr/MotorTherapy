using System;
using UnityEngine;

namespace CobWeb
{
    public class Goal : MonoBehaviour
    {
        public string word;
        public int points;
        public int i;
        public int j;
        private CardsManager _cardsManager;

        private void Start()
        {
            _cardsManager = GameObject.FindWithTag("Controller").GetComponent<CardsManager>();
        }

        private void OnCollisionEnter(Collision other)
        {
            if (!other.gameObject.CompareTag("Player")) return;
            _cardsManager.InstantiateCard(word, points);
            Destroy(gameObject);
        }
    }
}