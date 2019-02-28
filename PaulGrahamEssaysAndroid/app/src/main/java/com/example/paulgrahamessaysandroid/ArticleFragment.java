package com.example.paulgrahamessaysandroid;

import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.webkit.WebView;

public class ArticleFragment extends Fragment {
    WebView mWebView;

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        return inflater.inflate(R.layout.fragment_article, container, false);
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle bundle) {
        super.onViewCreated(view, bundle);
        bundle = this.getArguments();
        Log.v("articleFragment", bundle.toString());
        mWebView = getView().findViewById(R.id.articleView);
        if (bundle != null) {
            String articleName = bundle.getString(MainActivity.ARTICLE_NAME, "");
            String articleUrl = "file:///android_asset/articles/" + articleName;
            Log.v("articleFragment", articleUrl);
            mWebView.loadUrl(articleUrl);
        } else {
            // TODO: Handle null bundle with err msg
        }
        mWebView.getSettings().setJavaScriptEnabled(true);
    }
}
