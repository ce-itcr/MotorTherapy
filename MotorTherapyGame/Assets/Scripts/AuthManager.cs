using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class AuthManager : MonoBehaviour {

    protected Firebase.Auth.FirebaseAuth auth;
    protected Firebase.Auth.FirebaseUser user;
    private string displayName;

    [SerializeField] private InputField inputFieldEmail = null;
    [SerializeField] private InputField inputFieldPassword = null;

    [SerializeField] private GameObject LoginGroup = null;
    [SerializeField] private GameObject RegisterGroup = null;

    void Start()
    {
        InitializeFirebase();
    }

    void InitializeFirebase()
    {
        auth = Firebase.Auth.FirebaseAuth.DefaultInstance;
        auth.StateChanged += AuthStateChanged;
        AuthStateChanged(this, null);
    }

    void AuthStateChanged(object sender, System.EventArgs eventArgs)
    {
        if (auth.CurrentUser != user)
        {
            bool signedIn = user != auth.CurrentUser && auth.CurrentUser != null;
            if (!signedIn && user != null)
            {
                Debug.Log("Signed out " + user.UserId);
            }
            user = auth.CurrentUser;
            if (signedIn)
            {
                displayName = user.DisplayName ?? "";
                Debug.Log("Signed in " + user.UserId);
                
            }
        }
    }

    public void CreateUser()
    {
        string email = inputFieldEmail.text;
        string password = inputFieldPassword.text;

        auth.CreateUserWithEmailAndPasswordAsync(email, password).ContinueWith(task => {
            if (task.IsCanceled)
            {
                Debug.LogError("CreateUserWithEmailAndPasswordAsync was canceled.");
                return;
            }
            if (task.IsFaulted)
            {
                Debug.LogError("CreateUserWithEmailAndPasswordAsync encountered an error: " + task.Exception);
                return;
            }

            // Firebase user has been created.
            Firebase.Auth.FirebaseUser newUser = task.Result;
            Debug.LogFormat("Firebase user created successfully: {0} ({1})",
                newUser.DisplayName, newUser.UserId);

            ShowLoginGroup();
        });
    }

    public void LoginUser()
    {

        string email = inputFieldEmail.text;
        string password = inputFieldPassword.text;

        auth.SignInWithEmailAndPasswordAsync(email, password).ContinueWith(task => {
            if (task.IsCanceled)
            {
                Debug.LogError("SignInWithEmailAndPasswordAsync was canceled.");
                return;
            }
            if (task.IsFaulted)
            {
                Debug.LogError("SignInWithEmailAndPasswordAsync encountered an error: " + task.Exception);
                return;
            }

            Firebase.Auth.FirebaseUser newUser = task.Result;
            Debug.LogFormat("User signed in successfully: {0} ({1})",
                newUser.DisplayName, newUser.UserId);

            SceneManager.LoadScene("AppInterface");
        });
    }


    public void ShowLoginGroup()
    {
        LoginGroup.SetActive(true);
        RegisterGroup.SetActive(false);
    }

    public void ShowRegisterGroup()
    {
        LoginGroup.SetActive(false);
        RegisterGroup.SetActive(true);
    }
}
