package com.powermanager.powermanagerschedule.services;


import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Scanner;

public class CallApi {



    /**
     * @param url
     * @param bearer
     * @return
     * @throws IOException
     */
    public static String getState(String url, String bearer) throws IOException {
        URL url1 = new URL(url);
        HttpURLConnection httpConn = (HttpURLConnection) url1.openConnection();
        httpConn.setRequestMethod("GET");

        httpConn.setRequestProperty("Authorization", bearer);
        httpConn.setRequestProperty("Content-Type", "application/json");

        InputStream responseStream = httpConn.getResponseCode() / 100 == 2
                ? httpConn.getInputStream()
                : httpConn.getErrorStream();
        Scanner s = new Scanner(responseStream).useDelimiter("\\A");
        String response = s.hasNext() ? s.next() : "";
        return response;
    }

    /**
     * @param url
     * @param bearer
     * @throws IOException
     */
    public static void changeState(String url, String bearer) throws IOException {
        URL url3 = new URL(url);
        HttpURLConnection httpConn = (HttpURLConnection) url3.openConnection();
        httpConn.setRequestMethod("POST");

        httpConn.setRequestProperty("Authorization", bearer);
        httpConn.setRequestProperty("Content-Type", "application/json");

        httpConn.setDoOutput(true);
        OutputStreamWriter writer = new OutputStreamWriter(httpConn.getOutputStream());
        writer.write("{\"entity_id\": \"switch.develco\"}");
        writer.flush();
        writer.close();
        httpConn.getOutputStream().close();

        InputStream responseStream = httpConn.getResponseCode() / 100 == 2
                ? httpConn.getInputStream()
                : httpConn.getErrorStream();
        Scanner s = new Scanner(responseStream).useDelimiter("\\A");


    }

}

