namespace Piano
{
    public class TilesColors
    {
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
    }
    
    public enum Colors
    {
        Red, Green, Blue, Yellow, Black
    }
}
