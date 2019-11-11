package com.ceitcr.motortherapy.login;

import android.content.Context;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.firebase.auth.AuthResult;

public class SaveSharedPreferences {

    static final String email = "";
    static final String password = "";

    public static String getPassword(Context ctx) {
        return getSharedPreferences(ctx).getString(password, "");
    }

    public static void setPassword(Context ctx, String password) {
        SharedPreferences.Editor editor = getSharedPreferences((Context) ctx).edit();
        editor.putString(password, password);
        editor.commit();
    }

    public static String getEmail(Context ctx) {
        return getSharedPreferences(ctx).getString(email, "");
    }

    public static void setEmail(Context ctx, String password) {
        SharedPreferences.Editor editor = getSharedPreferences(ctx).edit();
        editor.putString(email, password);
        editor.commit();
    }


    static SharedPreferences getSharedPreferences(Context ctx) {
        return PreferenceManager.getDefaultSharedPreferences(ctx);
    }

    public static boolean IsLoged(Context ctx){
        if(getEmail(ctx).length()!=0 && getPassword(ctx).length()!=0){
            return true;
        }
        return false;
    }

    public static void CleanLogIn(Context ctx){
        setEmail(ctx,"");
        setPassword(ctx,"");
    }

}
