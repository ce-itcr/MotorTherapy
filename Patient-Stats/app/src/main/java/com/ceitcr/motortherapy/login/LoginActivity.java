package com.ceitcr.motortherapy.login;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.ceitcr.motortherapy.MainActivity;
import com.ceitcr.motortherapy.R;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;

public class LoginActivity extends AppCompatActivity {

    EditText input_email,input_password;
    Button button_sigin;
    FirebaseAuth mFirebaseAuth;
    private FirebaseAuth.AuthStateListener mAuthStateListener;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

//        getWindow().addFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN);

        mFirebaseAuth = FirebaseAuth.getInstance();
        input_email=findViewById(R.id.input_email);
        input_password=findViewById(R.id.input_password);
        button_sigin = findViewById(R.id.button_signin);
    }

    @Override
    public void onBackPressed() { moveTaskToBack(false); }


    public void validateInputFields(View view){

        String email = input_email.getText().toString();
        String password = input_password.getText().toString();

        if (email.isEmpty()){
            input_email.setError("Enter your email.");
            input_email.requestFocus();
        } else if (password.isEmpty()){
            input_password.setError("Enter your password.");
            input_password.requestFocus();
        } else if (email.isEmpty() && password.isEmpty()){
            Toast.makeText(this,"Please fill in all the spaces.", Toast.LENGTH_SHORT).show();
        } else if (!(email.isEmpty() && password.isEmpty())){
            mFirebaseAuth.signInWithEmailAndPassword(email,password).addOnCompleteListener(LoginActivity.this, new OnCompleteListener<AuthResult>() {
                @Override
                public void onComplete(@NonNull Task<AuthResult> task) {
                    if(!task.isSuccessful()){
                        Toast.makeText(LoginActivity.this, "Your email and password do not match.", Toast.LENGTH_SHORT).show();
                    }
                    else{
                        SaveSharedPreferences.setEmail(LoginActivity.this, input_email.getText().toString());
                        SaveSharedPreferences.setPassword(LoginActivity.this,input_password.getText().toString());
                        Intent mainActivity = new Intent(LoginActivity.this, MainActivity.class);
                        startActivity(mainActivity);
                        Toast.makeText(LoginActivity.this, "Welcome to MotorTherapy - Stats!", Toast.LENGTH_SHORT).show();
                    }
                }
            });

        }
    }
}
