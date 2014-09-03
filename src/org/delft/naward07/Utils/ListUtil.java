package org.delft.naward07.Utils;

import java.util.List;

/**
 * Utils for java.util.List
 *
 * Created by Feng Wang on 14-8-25.
 */

public class ListUtil {

    /**
     * Convert List<String> to String.
     * Using StringBuilder, it is fast. (At least, from StackOVerFlow...)
     *
     * @param list
     * @param delimiter
     * @return
     */
    public static String list2String(List<String> list, String delimiter){
        StringBuilder sb = new StringBuilder();

        String loopDelimiter = "";

        for(String s : list){
            sb.append(loopDelimiter);
            sb.append(s);

            loopDelimiter = delimiter;
        }

        return sb.toString();
    }
}
