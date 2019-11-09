using UnityEditor;
using UnityEngine;

namespace Piano
{
    public class TilesColors
    {
        private static Material[] _colorsMesh = LoadMeshColors();
        
        public static Colors[] ToColorsFromString(string[] colorsStr)
        {
            var colors = new Colors[colorsStr.Length];
            for (var i = 0; i < colorsStr.Length; i++)
            {
                colors[i] = ToColor(colorsStr[i]);
            }

            return colors;
        }

        private static Colors ToColor(string colorStr)
        {
            var color = Colors.Black;
            switch (colorStr.ToLower())
            {
                case "red":
                    color = Colors.Red;
                    break;
                case "green":
                    color = Colors.Green;
                    break;
                case "yellow":
                    color = Colors.Yellow;
                    break;
                case "blue":
                    color = Colors.Blue;
                    break;
            }

            return color;
        }

        public static Material RandomMeshColor()
        {
            var i = Random.Range(0, _colorsMesh.Length);
            return _colorsMesh[i];
        }

        private static Material[] LoadMeshColors()
        {
            const string path = "Colors";
            return Resources.LoadAll<Material>(path);
        }
    }
    
    public enum Colors
    {
        Red, Green, Blue, Yellow, Black
    }
}
