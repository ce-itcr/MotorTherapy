package com.ceitcr.motortherapy.login;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.ceitcr.motortherapy.MainActivity;
import com.ceitcr.motortherapy.R;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;

import static android.widget.Toast.LENGTH_SHORT;

public class RegisterActivity extends AppCompatActivity {

    EditText input_email,input_password;
    Button button_sigup;
    FirebaseAuth mFirebaseAuth;
    private static final String TAG = "RegisterActivity";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);

        getWindow().addFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN);

        mFirebaseAuth = FirebaseAuth.getInstance();
        input_email=findViewById(R.id.input_email);
        input_password=findViewById(R.id.input_password);
        button_sigup = findViewById(R.id.button_signup);

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
            Toast.makeText(this,"Please fill in all the spaces.", LENGTH_SHORT).show();
        } else if (!(email.isEmpty() && password.isEmpty())){
            mFirebaseAuth.createUserWithEmailAndPassword(email,password)
                    .addOnCompleteListener(RegisterActivity.this, new OnCompleteListener<AuthResult>() {
                        @Override
                        public void onComplete(@NonNull Task<AuthResult> task) {
                            Log.d(TAG, "New user registration: " + task.isSuccessful());

                            if (!task.isSuccessful()) {
//                                RegisterActivity.this.showToast("Authentication failed. " + task.getException());
                                Toast.makeText(getBaseContext(), "Authentication failed. " + task.getException(), LENGTH_SHORT).show();
                            } else {
                                RegisterActivity.this.startActivity(new Intent(RegisterActivity.this, MainActivity.class));
                                Toast.makeText(RegisterActivity.this, "Welcome to MotorTherapy.", Toast.LENGTH_SHORT).show();
                                RegisterActivity.this.finish();
                            }
                        }
                    });

        }

    }

    public void toLogin(View view){
        Intent i = new Intent(getBaseContext(), LoginActivity.class);
        startActivity(i);
    }
}
