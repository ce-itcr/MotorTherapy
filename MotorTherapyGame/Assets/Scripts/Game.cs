using System;
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
    public string status;
    public Piano piano;
    public Targets targets;
    public CobWeb cobWeb;
    public Balloons balloons;

    public Game() {}
    
    
    public Game(string type, string status)
    {
        this.type = type;
        this.status = status;
    }
    
    
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
    public struct Balloons
    {
        public int x;
        public int y;
    }
}
