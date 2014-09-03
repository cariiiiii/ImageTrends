/**
 * Created by Feng Wang on 14-7-14.
 */

package org.delft.naward07.MapReduce.hadoop.warc;

import java.io.*;

import org.delft.naward07.Utils.ImageUtils.ImageHelper;
import org.apache.http.client.utils.DateUtils;

import org.jwat.warc.WarcRecord;
import org.jwat.common.HttpHeader;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

/**
 * Extract hash code from the WARC record.
 *
 * @author Feng Wang
 */
public class Record2Hashcode {
    private static final int MAX_PAYLOAD = 1000000;

    Record2Hashcode() {}

    /**
     * Check if every part in the hash code satisfy the pre-defined rules (not empty).
     * If not, return "".
     *
     * @param finger image finger
     * @param lastModified last modified time
     * @param url url of image
     * @return hash code or ""
     */
    private static String checkItems(String finger, String lastModified, String url) {
        try {
            if ("".equals(finger) || ("".equals(lastModified)) || "".equals(url))
                return "";
        } catch (Exception e) {
            return "";
        }

        //if (!"".equals(lastModified))
        return finger + "|" + lastModified + "|" + url;

        //else return finger + "|" + date + "|" + url;
    }

    /**
     * Get the target URL from the WARC record.
     *
     * @param record WARC record
     * @return Target URL
     */
    private static String getURL(WarcRecord record){
        return record.header.warcTargetUriStr;
    }

    /**
     * Get the "Last-Modified" field in the HTTP header.
     *
     * @param header HTTP header
     * @return Last-Modified date
     */
    private static String getLastModified(HttpHeader header){
        String lastModified = "";
        DateFormat df = new SimpleDateFormat("yyyyMMdd");

        try {
            lastModified = header.getHeader("Last-Modified").value;
            Date tempD1 = DateUtils.parseDate(lastModified);
            lastModified = df.format(tempD1);

        } catch (Exception e) {
        }

        if (!lastModified.matches("[0-9]*")) {
            int ind = lastModified.lastIndexOf(" ");
            lastModified = lastModified.substring(0, ind) + " GMT";
            Date tempD1 = DateUtils.parseDate(lastModified);
            lastModified = df.format(tempD1);
        }

        return lastModified;
    }

    /**
     * Get hash code from a record.
     *
     * @param record WARC record
     * @return hash code
     */
    public static String getHashcode(WarcRecord record) {
        try {
            HttpHeader httpHeader = record.getHttpHeader();
            if (httpHeader == null) {
                return "";
            } else if (httpHeader.contentType != null && httpHeader.contentType.contains("image")) {
                InputStream inputStream1 = null;

                if (record.getPayload().getTotalLength() > MAX_PAYLOAD)
                    return "";

                inputStream1 = record.getPayload().getInputStream();

                String url = getURL(record);
                System.out.println("url: " + url);

//                byte[] b1 = IOUtils.toByteArray(inputStream1);
//                byte[] encoded = Base64.encodeBase64(b1);
//                String finger = new String(encoded, "US-ASCII");

                String finger = ImageHelper.imageFingerPrint(inputStream1);
                String lastModified = getLastModified(httpHeader);

                return checkItems(finger, lastModified, url);

            } else {
                return "";
            }
        } catch (Exception e) {
            //e.printStackTrace();
            return "";
        }
    }

}
