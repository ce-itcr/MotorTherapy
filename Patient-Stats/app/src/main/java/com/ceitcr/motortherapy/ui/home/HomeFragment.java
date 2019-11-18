package com.ceitcr.motortherapy.ui.home;

import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.Observer;
import androidx.lifecycle.ViewModelProviders;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;
import com.ceitcr.motortherapy.R;
import com.ceitcr.motortherapy.util.RecyclerViewAdapter;

import java.util.ArrayList;

public class HomeFragment extends Fragment {

    private static final String TAG = "HomeActivity";

    private ArrayList<String> mNames = new ArrayList<>();
    private ArrayList<String> mImageUrls = new ArrayList<>();


    private HomeViewModel homeViewModel;

    public View onCreateView(@NonNull LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {

        homeViewModel =
                ViewModelProviders.of(this).get(HomeViewModel.class);
        View root = inflater.inflate(R.layout.fragment_home, container, false);

        initImageBitmaps(root);

        return root;

    }

    private void initImageBitmaps(View root){
        Log.d(TAG, "initImageBitmaps: preparing bitmaps.");

        mImageUrls.add("https://www.it.iitb.ac.in/frg/wiki/images/thumb/d/dc/User.jpg/960px-User.jpg");
        mNames.add("TestPacient");
        mImageUrls.add("https://www.it.iitb.ac.in/frg/wiki/images/thumb/d/dc/User.jpg/960px-User.jpg");
        mNames.add("TestPacient");
        mImageUrls.add("https://www.it.iitb.ac.in/frg/wiki/images/thumb/d/dc/User.jpg/960px-User.jpg");
        mNames.add("TestPacient");
        mImageUrls.add("https://www.it.iitb.ac.in/frg/wiki/images/thumb/d/dc/User.jpg/960px-User.jpg");
        mNames.add("TestPacient");
        mImageUrls.add("https://www.it.iitb.ac.in/frg/wiki/images/thumb/d/dc/User.jpg/960px-User.jpg");
        mNames.add("TestPacient");
        mImageUrls.add("https://www.it.iitb.ac.in/frg/wiki/images/thumb/d/dc/User.jpg/960px-User.jpg");
        mNames.add("TestPacient");
        mImageUrls.add("https://www.it.iitb.ac.in/frg/wiki/images/thumb/d/dc/User.jpg/960px-User.jpg");
        mNames.add("TestPacient");

        initRecyclerView(root);
    }

    private void initRecyclerView(View root){
        Log.d(TAG, "initRecyclerView: init recyclerview.");
        RecyclerView recyclerView = root.findViewById(R.id.recycler_View);
        RecyclerViewAdapter adapter = new RecyclerViewAdapter(getActivity(), mNames, mImageUrls);
        recyclerView.setAdapter(adapter);
        recyclerView.setLayoutManager(new LinearLayoutManager(getActivity()));
    }


}