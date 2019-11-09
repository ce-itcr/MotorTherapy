package com.ceitcr.motortherapy;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;
import androidx.fragment.app.Fragment;

import android.app.ActionBar;
import android.content.Context;
import android.content.Intent;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.view.WindowManager;

import com.ceitcr.motortherapy.login.LoginActivity;
import com.ceitcr.motortherapy.login.SaveSharedPreferences;
import com.github.paolorotolo.appintro.AppIntro;
import com.github.paolorotolo.appintro.AppIntroFragment;

public class IntroActivity extends AppIntro {

    @RequiresApi(api = Build.VERSION_CODES.JELLY_BEAN)
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN);

        if (SaveSharedPreferences.IsLoged(this)){
            //Toast.makeText(this, "Previamente logeado", Toast.LENGTH_LONG).show();
            Intent intSignUp = new Intent(this, MainActivity.class);
            startActivity(intSignUp);
        }
        ConnectivityManager connectivityManager = (ConnectivityManager)getSystemService(Context.CONNECTIVITY_SERVICE);
        if(connectivityManager.getNetworkInfo(ConnectivityManager.TYPE_MOBILE).getState() == NetworkInfo.State.CONNECTED ||
                connectivityManager.getNetworkInfo(ConnectivityManager.TYPE_WIFI).getState() == NetworkInfo.State.CONNECTED) {
            //we are connected to a network

        }
        else{
            AlertDialog.Builder builder = new AlertDialog.Builder(this);

            builder.setMessage("Revise su conexión a wifi")
                    .setTitle("Wifi no detectado");

            AlertDialog dialog = builder.create();

            dialog.show();
        }

        addSlide(AppIntroFragment.newInstance("First Page","This is the First Description",R.drawable.ic_launcher, ContextCompat.getColor(getApplicationContext(),R.color.colorIntro)));
        addSlide(AppIntroFragment.newInstance("Second Page","This is the Second Description",R.drawable.ic_launcher, ContextCompat.getColor(getApplicationContext(),R.color.colorIntro)));
        addSlide(AppIntroFragment.newInstance("Third Page","This is the Third Description",R.drawable.ic_launcher, ContextCompat.getColor(getApplicationContext(),R.color.colorIntro)));
    }

    @Override
    public void onDonePressed(Fragment currentFragment){
        super.onDonePressed(currentFragment);
        startActivity(new Intent(getApplicationContext(), LoginActivity.class));
    }

    @Override
    public void onSkipPressed(Fragment currentFragment){
        super.onSkipPressed(currentFragment);
        startActivity(new Intent(getApplicationContext(), LoginActivity.class));
    }
}
