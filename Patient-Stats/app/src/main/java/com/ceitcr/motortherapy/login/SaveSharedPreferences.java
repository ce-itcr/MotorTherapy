package com.ceitcr.motortherapy.login;

import android.content.Context;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;

public class SaveSharedPreferences {
    static final String email = "";
    static final String password = "";

    public static String getpassword(Context ctx) {
        return getSharedPreferences(ctx).getString(password, "");
    }

    public static void setpassword(Context ctx, String password) {
        SharedPreferences.Editor editor = getSharedPreferences(ctx).edit();
        editor.putString(password, password);
        editor.commit();
    }

    public static String getemail(Context ctx) {
        return getSharedPreferences(ctx).getString(email, "");
    }

    public static void setemail(Context ctx, String password) {
        SharedPreferences.Editor editor = getSharedPreferences(ctx).edit();
        editor.putString(email, password);
        editor.commit();
    }


    static SharedPreferences getSharedPreferences(Context ctx) {
        return PreferenceManager.getDefaultSharedPreferences(ctx);
    }

    public static boolean IsLoged(Context ctx){
        if(getemail(ctx).length()!=0 && getpassword(ctx).length()!=0){
            return true;
        }
        return false;
    }

    public static void CleanLogIn(Context ctx){
        setemail(ctx,"");
        setpassword(ctx,"");
    }

}
