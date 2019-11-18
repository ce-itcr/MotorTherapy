using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;


[Serializable]
public class User
{
    public string userName;
    public int userScore;

    public User()
    {
        userName = PatientStats.playerName;
        userScore = PatientStats.playerScore;
    }

}