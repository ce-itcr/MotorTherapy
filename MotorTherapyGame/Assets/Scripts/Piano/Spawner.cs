using System;
using System.Collections;
using System.Threading;
using UnityEditor;
using UnityEngine;

namespace Piano
{
    public class Spawner : MonoBehaviour
    {
        public Transform redPianoFlag;
        public Transform bluePianoFlag;
        public Transform greenPianoFlag;
        public Transform yellowPianoFlag;
        public GameObject notePrefab;
        private Colors[] _colors;
        private int[] _points;
        private float _time;
        private bool _finished;
        private int _spawnCount;

        private void Update()
        {
            if (FindObjectsOfType<Note>().Length <= 0 && _spawnCount <= 0) _finished = true;
        }

        public void Spawn(string[] colorsStr, int[] points, int time)
        {
            if (colorsStr == null) return;
            _finished = false;
            _colors = TilesColors.ToColorsFromString(colorsStr);
            _points = points;
            _time = (float) time / _colors.Length;
            _spawnCount = _colors.Length;
            StartCoroutine(nameof(SpawnEach));
        }

        private IEnumerator SpawnEach()
        {
            for (var i = 0; i < _colors.Length; i++)
            {
                CreateNote(_colors[i], _points[i]);
                _spawnCount--;
                if (i == _colors.Length) yield break;
                yield return new WaitForSeconds(_time);
            }
        }

        private void CreateNote(Colors color, int points)
        {
            var position = transform.position;
            float x;
            var y = position.y;
            var z = position.z;
            Material material = null;

            switch (color)
            {
                case Colors.Red:
                    x = redPianoFlag.transform.position.x;
                    material = redPianoFlag.GetComponent<MeshRenderer>().sharedMaterial;
                    break;
                case Colors.Green:
                    x = greenPianoFlag.transform.position.x;
                    material = greenPianoFlag.GetComponent<MeshRenderer>().sharedMaterial;
                    break;
                case Colors.Blue:
                    x = bluePianoFlag.transform.position.x;
                    material = bluePianoFlag.GetComponent<MeshRenderer>().sharedMaterial;
                    break;
                case Colors.Yellow:
                    x = yellowPianoFlag.transform.position.x;
                    material = yellowPianoFlag.GetComponent<MeshRenderer>().sharedMaterial;
                    break;
                default:
                    throw new ArgumentOutOfRangeException(nameof(color), color, null);
            }

            var note = Instantiate(notePrefab, new Vector3(x, y, z), notePrefab.transform.rotation);
            note.GetComponent<MeshRenderer>().sharedMaterial = material;
            // (Note) note.points = points;

        }

        public bool Finished => _finished;
    }
}
