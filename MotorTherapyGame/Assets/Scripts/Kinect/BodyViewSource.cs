using System.Collections.Generic;
using Windows.Kinect;
using UnityEngine;
using Joint = Windows.Kinect.Joint;

public class BodyViewSource : MonoBehaviour
{
    public BodySourceManager bodySourceManager;
    public GameObject jointCollider;
    public float targetZ;
    
    private readonly Dictionary<ulong, GameObject> _bodies = new Dictionary<ulong, GameObject>();

    private readonly List<JointType> _joints = new List<JointType>
    {
        JointType.HandLeft,
        JointType.HandRight,
        JointType.FootLeft,
        JointType.FootRight,
    };

    private void Update () 
    {
        #region Gets the Kinect data
        var data = bodySourceManager.GetData();
        if (data == null) return;

        var trackedIds = new List<ulong>();
        foreach(var body in data)
        {
            if (body == null) continue;

            if(body.IsTracked)
                trackedIds.Add (body.TrackingId);
        }
        #endregion

        #region Delete Kinect bodies
        var knownIds = new List<ulong>(_bodies.Keys);
        foreach(var trackingId in knownIds)
        {
            if (trackedIds.Contains(trackingId)) continue;
            Destroy(_bodies[trackingId]);
            _bodies.Remove(trackingId);
        }
        #endregion

        #region Create Kinect bodies
        foreach(var body in data)
        {
            if (body == null) continue;
            if (!body.IsTracked) continue;
            
            // Creates the body if isn't tracked
            if(!_bodies.ContainsKey(body.TrackingId))
                _bodies[body.TrackingId] = CreateBodyObject(body.TrackingId);

            // Updates position
            UpdateBodyObject(body, _bodies[body.TrackingId]);
        }
        #endregion
    }
    
    private GameObject CreateBodyObject(ulong id)
    {
        var body = new GameObject("Body:" + id);
        
        // Create joints
        foreach (var joint in _joints)
        {
            var jointObj = Instantiate(jointCollider, body.transform, true);
            jointObj.name = joint.ToString();
        }
        
        return body;
    }
    
    private void UpdateBodyObject(Body body, GameObject bodyObject)
    {
        foreach (var joint in _joints)
        {
            // Get new position
            var sourceJoint = body.Joints[joint];
            var position = GetVector3FromJoint(sourceJoint);
            position.z = targetZ;
            
            // Set new position
            var jointObj = bodyObject.transform.Find(joint.ToString());
            jointObj.position = position;
        }
    }

    private static Vector3 GetVector3FromJoint(Joint joint)
    {
        return new Vector3(joint.Position.X * 10, joint.Position.Y * 10, joint.Position.Z * 10);
    }

}
