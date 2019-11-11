package com.ceitcr.motortherapy;

import android.content.Context;
import android.content.Intent;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.os.Bundle;
import android.view.WindowManager;

import androidx.appcompat.app.AlertDialog;
import androidx.core.content.ContextCompat;
import androidx.fragment.app.Fragment;

import com.ceitcr.motortherapy.login.LoginActivity;
import com.ceitcr.motortherapy.login.SaveSharedPreferences;
import com.github.paolorotolo.appintro.AppIntro;
import com.github.paolorotolo.appintro.AppIntroFragment;

public class IntroActivity extends AppIntro {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN);

        if (SaveSharedPreferences.IsLoged(this)){
            Intent intSignUp = new Intent(this, MainActivity.class);
            startActivity(intSignUp);
        }
        ConnectivityManager connectivityManager = (ConnectivityManager)getSystemService(Context.CONNECTIVITY_SERVICE);
        if(connectivityManager.getNetworkInfo(ConnectivityManager.TYPE_MOBILE).getState() == NetworkInfo.State.CONNECTED ||
                connectivityManager.getNetworkInfo(ConnectivityManager.TYPE_WIFI).getState() == NetworkInfo.State.CONNECTED) {
        }
        else{
            AlertDialog.Builder builder = new AlertDialog.Builder(this);

            builder.setMessage("Check your internet connection.")
                    .setTitle("Wifi not detected.");

            AlertDialog dialog = builder.create();

            dialog.show();
        }

        addSlide(AppIntroFragment.newInstance("","Step 1. Sign In.",R.drawable.ic_launcher, ContextCompat.getColor(getApplicationContext(),R.color.colorPrimary)));
        addSlide(AppIntroFragment.newInstance("","Step 2. Select a Patient.",R.drawable.ic_launcher, ContextCompat.getColor(getApplicationContext(),R.color.colorPrimary)));
        addSlide(AppIntroFragment.newInstance("","Step 3. Visualize in real time the statistics of said patient.",R.drawable.ic_launcher, ContextCompat.getColor(getApplicationContext(),R.color.colorPrimary)));
    }

    @Override
    public void onDonePressed(Fragment currentFragment) {
        super.onDonePressed(currentFragment);
        startActivity(new Intent(getApplicationContext(), LoginActivity.class));
    }

    @Override
    public void onSkipPressed(Fragment currentFragment) {
        super.onSkipPressed(currentFragment);
        startActivity(new Intent(getApplicationContext(),LoginActivity.class));

    }

}
