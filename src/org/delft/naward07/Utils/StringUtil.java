package org.delft.naward07.Utils;

import java.math.BigInteger;

/**
 * Utils for String.
 *
 * Created by Feng Wang on 14-8-27.
 */

public class StringUtil {

    /**
     * Hex string to binary.
     *
     * @param Hex Hex string.
     * @return Corresponding binary string.
     */
    public static String hex2Binary(String Hex) {
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < Hex.length(); i ++){
            String bin = new BigInteger(Hex.substring(i, i + 1), 16).toString(2);
            while (bin.length() < 4)
                bin = "0" + bin;
            sb.append(bin);
        }
        return sb.toString();
    }
}
