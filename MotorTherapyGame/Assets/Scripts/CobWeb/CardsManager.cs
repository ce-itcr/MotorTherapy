using System;
using UnityEngine;

namespace CobWeb
{
    public class CardsManager : MonoBehaviour
    {
        public Transform cardsUi;
        public GameObject cardPref;
        private const float Offset = -0.75f;
        private GameObject _cobWeb;

        private void Start()
        {
            _cobWeb = GameObject.FindWithTag("Controller");
        }

        public void InstantiateCard(string word, int points)
        {
            var cardIns = Instantiate(cardPref, cardsUi);

            // Sets Position
            var x = cardsUi.childCount + Offset;
            if (cardsUi.childCount > 0)
            {
                MoveCards();
                x = cardsUi.GetChild(cardsUi.childCount - 1).localPosition.x - Offset * 2;
            }
            var poss = new Vector3(x, 0 , 0);
            cardIns.transform.localPosition = poss;
            
            // Manage Score
            _cobWeb.SendMessage("AddScore", points);
        }

        private void MoveCards()
        {
            foreach (Transform card in cardsUi)
            {
                card.Translate(Offset / 2, 0, 0);
            }
        }

    }
}
