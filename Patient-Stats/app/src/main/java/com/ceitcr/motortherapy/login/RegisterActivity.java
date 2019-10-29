package com.ceitcr.motortherapy.login;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.ceitcr.motortherapy.MainActivity;
import com.ceitcr.motortherapy.R;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;

public class RegisterActivity extends AppCompatActivity {
    EditText emailId,password;
    Button btnSignUp;
    TextView tvSignIn;
    FirebaseAuth mFirebaseAuth;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mFirebaseAuth = FirebaseAuth.getInstance();
        emailId=findViewById(R.id.editText);
        password=findViewById(R.id.editText2);
        btnSignUp = findViewById(R.id.button);
        tvSignIn = findViewById(R.id.textView);
        btnSignUp.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                final String email = emailId.getText().toString();
                String pwd = password.getText().toString();
                if (email.isEmpty()){
                    emailId.setError("Please Enter Email Id");
                    emailId.requestFocus();
                }
                else if (pwd.isEmpty()){
                    password.setError("Please Enter Your Password");
                    password.requestFocus();
                }
                else if (email.isEmpty() && pwd.isEmpty()){
                    Toast.makeText(RegisterActivity.this, "Fields are Empty", Toast.LENGTH_SHORT).show();
                }
                else if(!(email.isEmpty() && pwd.isEmpty())){
                    mFirebaseAuth.createUserWithEmailAndPassword(email,pwd).addOnCompleteListener(RegisterActivity.this, new OnCompleteListener<AuthResult>() {
                        @Override
                        public void onComplete(@NonNull Task<AuthResult> task) {
                            if(!task.isSuccessful()){
                                Toast.makeText(RegisterActivity.this, "Sign Up Unsuccessful", Toast.LENGTH_SHORT).show();
                            }
                            else {
                                startActivity(new Intent(RegisterActivity.this,MainActivity.class));

//                                ActionCodeSettings actionCodeSettings =
//                                        ActionCodeSettings.newBuilder()
//                                                // URL you want to redirect back to. The domain (www.example.com) for this
//                                                // URL must be whitelisted in the Firebase Console.
//                                                .setUrl("https://www.example.com/finishSignUp?cartId=1234")
//                                                // This must be true
//                                                .setHandleCodeInApp(true)
//                                                .setIOSBundleId("com.example.ios")
//                                                .setAndroidPackageName(
//                                                        "com.example.android",
//                                                        true, /* installIfNotAvailable */
//                                                        "12"    /* minimumVersion */)
//                                                .build();
//
//
//                                FirebaseAuth auth = FirebaseAuth.getInstance();
//                                auth.sendSignInLinkToEmail(email, actionCodeSettings)
//                                        .addOnCompleteListener(new OnCompleteListener<Void>() {
//                                            @Override
//                                            public void onComplete(@NonNull Task<Void> task) {
//                                                if (task.isSuccessful()) {
//                                                    Log.d(TAG, "Email sent.");
//                                                }
//                                            }
//                                        });

                            }
                        }
                    });
                }
                else {
                    Toast.makeText(RegisterActivity.this, "Error Ocurred", Toast.LENGTH_SHORT).show();
                }
            }

        });

        tvSignIn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i = new Intent(RegisterActivity.this,LoginActivity.class);
                startActivity(i);
            }
        });
    }
}
