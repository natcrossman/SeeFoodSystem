package ceg4110.wright.edu.seefoodclient;

import android.annotation.SuppressLint;
import android.content.Context;
import android.content.Intent;
import android.graphics.drawable.Drawable;
import android.net.Uri;
import android.os.AsyncTask;
import android.os.Build;
import android.os.Bundle;
import android.os.Environment;
import android.provider.MediaStore;
import android.support.annotation.RequiresApi;
import android.support.v4.content.FileProvider;
import android.support.v4.view.ViewPager;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ImageView;
import android.widget.Spinner;

import org.json.JSONArray;
import org.json.JSONException;

import java.io.File;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.OkHttpClient;
import okhttp3.RequestBody;

/**
 * Created by Don Miller
 */

public class MainActivity extends AppCompatActivity implements ASyncResponse{

    ImageAdapter adapter;
    static final int REQUEST_TAKE_PHOTO = 1;
    String mCurrentPhotoPath;
    Context context;
    int pagerSize;
    ASyncResponse asr;
    JSONProcessor processor;
    ImageView view;
    ViewPager pager;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        context = getApplicationContext();
        setContentView(R.layout.activity_main);
        adapter = new ImageAdapter();
        asr = this;
        pager = (ViewPager) findViewById(R.id.viewPager);
        pager.setAdapter(adapter);

        // The process for inserting an image into the ViewPager.
        // This is the ur-process which I replicated throughout the project.
        // 1. Instantiate the ImageView
        ImageView startImage = new ImageView(this);
        // 2. Convert image to Drawable object
        Drawable myIcon = getResources().getDrawable(R.drawable.ic_launcher);
        // 3. call setImageDrawable on the ImageView
        startImage.setImageDrawable(myIcon);
        // 4. Add the view using the adapter's method
        addImageView(startImage);

        Spinner dropdown = (Spinner) findViewById(R.id.spinner);
        dropdown.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                switch (position) {
                    case 0:
                        break;
                    // Case 1 should implement "browse server gallery"
                    case 1:
                        break;
                    case 2:
                        System.exit(0);
                }
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {

            }
        });
    }

    // Camera method shamelessly adapted from official Android documentation
    public void dispatchTakePictureIntent(View v) {
        Intent takePictureIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);

        // Ensure that there's a camera activity to handle the intent
        if (takePictureIntent.resolveActivity(getPackageManager()) != null) {

            // Create the File where the photo should go
            File photoFile = null;
            try {
                photoFile = createImageFile();
            } catch (IOException ex) {
                ex.printStackTrace();
            }
            // Continue only if the File was successfully created
            if (photoFile != null) {
                Uri photoURI = FileProvider.getUriForFile(context,
                        "ceg4110.wright.edu.seefoodclient.android.fileprovider",
                        photoFile);
                takePictureIntent.putExtra(MediaStore.EXTRA_OUTPUT, photoURI);
                startActivityForResult(takePictureIntent, REQUEST_TAKE_PHOTO);
            }
        }
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        // Check which request we're responding to
        if (requestCode == REQUEST_TAKE_PHOTO) {
            // Make sure the request was successful
            if (resultCode == RESULT_OK) {
                File imageFile = new File(mCurrentPhotoPath);

                try {
                    uploadImage(imageFile);
                } catch (IOException | JSONException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    // createImageFile() creates and names the file object for use by the camera intent
    private File createImageFile() throws IOException {
        // Create image file name
        String timeStamp = new SimpleDateFormat("yyyyMMdd_HHmmss", Locale.US).format(new Date());
        String imageFileName = "JPEG_" + timeStamp + "_";
        File storageDir = getExternalFilesDir(Environment.DIRECTORY_PICTURES);
        File image = File.createTempFile(
                imageFileName,  /* prefix */
                ".jpg",         /* suffix */
                storageDir      /* directory */
        );
        // Save a file in a global String variable: path for use with ACTION_VIEW intents
        mCurrentPhotoPath = image.getAbsolutePath();
        return image;
    }

    private void uploadImage(File imageFile) throws IOException, JSONException {

        MediaType mediaType = MediaType.parse("image/jpeg");
        OkHttpHandler handler = new OkHttpHandler(mediaType, imageFile, asr);

        handler.execute();
    }


    // ProcessFinish() catches the server response from the ASync thread
    // and sends it to a JSONProcessor for addition to the central ViewPager.
    @RequiresApi(api = Build.VERSION_CODES.M)
    @Override
    public void processFinish(JSONArray output, File imageFile) {

        Drawable imageDrawable = Drawable.createFromPath(imageFile.getAbsolutePath());
        processor = new JSONProcessor(imageDrawable, context);
        try {
            view = processor.processJSONData(output);
        } catch (JSONException e) {
            e.printStackTrace();
        }
        addImageView(view);
    }

    // Method to simplify the process of adding to the ViewPager
    private void addImageView(View v){
        pagerSize = adapter.addView (v);
        pager.setCurrentItem (pagerSize, true);
    }

    ////////////////////////////////////////////////////////////////////////////////////////////////
    //BEGIN PRIVATE ASYNCTASK CLASS ////////////////////////////////////////////////////////////////

    // The ASyncTask is constructed as a private subclass to ensure that
    // the processFinish method can always find the correct UI thread.
    @SuppressLint("StaticFieldLeak")
    private class OkHttpHandler extends AsyncTask<Void, Void, String> {

        ASyncResponse delegate;
        MediaType mediaType;
        File imageFile;
        okhttp3.Response response;
        JSONArray output = null;

        OkHttpHandler(MediaType newType, File newFile, ASyncResponse asr) {
            super();
            mediaType = newType;
            imageFile = newFile;
            delegate = asr;
        }

        // doInBackground holds the logic for the core "upload image/receive json" functionality
        @Override
        protected String doInBackground(Void... voids) {

            OkHttpClient client = new OkHttpClient();
            String string = null;

            RequestBody requestBody = new MultipartBody.Builder()
                    .setType(MultipartBody.FORM)
                    .addFormDataPart("file", imageFile.getName(),
                            RequestBody.create(MediaType.parse("image/jpeg"), imageFile))
                    .build();

            okhttp3.Request request = new okhttp3.Request.Builder()
                    .url("http://34.237.62.217/evaluation")
                    .post(requestBody)
                    .addHeader("content-type", "multipart/form-data")
                    .build();
            try {
                response = client.newCall(request).execute();
            } catch (IOException e) {
                e.printStackTrace();
            }

            try {
                string = response.body().string();
            } catch (IOException e) {
                e.printStackTrace();
            }

            return string;
        }

        // Here we convert the server's response into a JSONArray which is passed back to the main thread
        @Override
        protected void onPostExecute(String s) {
            super.onPostExecute(s);

            try {
                Log.e("String", s);
                output = new JSONArray(s);
            } catch (JSONException e) {
                e.printStackTrace();
            }

            delegate.processFinish(output, imageFile);
        }
    }
}
