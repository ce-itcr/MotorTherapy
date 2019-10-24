using System;
using System.Collections.Generic;
using UnityEngine;

/**
 * @Author Jose Acuna
 * Last time edited 23/10/19 by Jose Acuna
 * @Reference https://docs.unity3d.com/ScriptReference/JsonUtility.FromJson.html
 */
[Serializable]
public class Game
{
    public string type;
    public Piano piano;
    public Targets targets;
    public CobWeb cobWeb;
    public Ballons ballons;
    
    
    public static Game CreateFromJson(string json)
    {
        return JsonUtility.FromJson<Game>(json);
    }
    
    
    [Serializable]
    public struct Piano
    {
        public string[] colors;
        public int[] points;
        public int time;
    }
    
    [Serializable]
    public struct Targets
    {
        public int x;
        public int y;
        public int time;
    }
    
    [Serializable]
    public struct CobWeb
    {
        public Card[] cards;
        
        [Serializable]
        public struct Card
        {
            public string name;
            public int points;
            public int i;
            public int j;
        }
    }
    
    [Serializable]
    public struct Ballons
    {
        public int x;
        public int y;
    }
}
