using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;

public class Spawner : MonoBehaviour
{

    public Transform redPianoFlag;
    public Transform bluePianoFlag;
    public Transform greenPianoFlag;
    public Transform yellowPianoFlag;
    public GameObject notePrefab;

    // Start is called before the first frame update
    void Start()
    {
        StartCoroutine(TestNotes());
    }

    private IEnumerator TestNotes()
    {
        createNote(TilesColors.Colors.Red);
        yield return new WaitForSeconds(2);
        createNote(TilesColors.Colors.Green);
        yield return new WaitForSeconds(1);
        createNote(TilesColors.Colors.Blue);
        yield return new WaitForSeconds(1);
        createNote(TilesColors.Colors.Yellow);
        yield return new WaitForSeconds(2);
        createNote(TilesColors.Colors.Green);
        yield return new WaitForSeconds(1);
        createNote(TilesColors.Colors.Yellow);
    }

    private void createNote(TilesColors.Colors color)
    {
        float x = transform.position.x;
        float y = transform.position.y;
        float z = transform.position.z;
        Material material = null;

        switch (color)
        {
            case TilesColors.Colors.Red:
                x = redPianoFlag.transform.position.x;
                material = redPianoFlag.GetComponent<MeshRenderer>().sharedMaterial;
                break;
            case TilesColors.Colors.Green:
                x = greenPianoFlag.transform.position.x;
                material = greenPianoFlag.GetComponent<MeshRenderer>().sharedMaterial;
                break;
            case TilesColors.Colors.Blue:
                x = bluePianoFlag.transform.position.x;
                material = bluePianoFlag.GetComponent<MeshRenderer>().sharedMaterial;
                break;
            case TilesColors.Colors.Yellow:
                x = yellowPianoFlag.transform.position.x;
                material = yellowPianoFlag.GetComponent<MeshRenderer>().sharedMaterial;
                break;
        }

        GameObject note = Instantiate(notePrefab, new Vector3(x, y, z), notePrefab.transform.rotation);
        note.GetComponent<MeshRenderer>().sharedMaterial = material;
    }
}
