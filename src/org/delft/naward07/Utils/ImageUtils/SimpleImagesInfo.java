package org.delft.naward07.Utils.ImageUtils;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * Store images' information. Used in HashMap.
 *
 * Created by Feng Wang on 14-8-3.
 */
public class SimpleImagesInfo implements Comparable<SimpleImagesInfo> {
    private List<String> hashcodes;
    private Set<String> hosts;
    private int number = 1;

    /**
     * Constructor.
     *
     * @param hashcode Image hash code.
     * @param host Image host.
     */
    public SimpleImagesInfo(String hashcode, String host){
        hashcodes = new ArrayList<String>();
        hashcodes.add(hashcode);
        hosts = new HashSet<String>();
        hosts.add(host);
    }

    /**
     * If the host is not in the hosts list, then increase the number.
     *
     * @param host Image host.
     * @return
     */
    public boolean increment(String host){
        if (hosts.contains(host))
            return false;
        number++;
        hosts.add(host);
        return true;
    }

    /**
     * Update the hashcodes and hosts.
     *
     * @param hashcode Image hash code.
     * @param host Image host.
     */
    public void update(String hashcode, String host){
        hashcodes.add(hashcode);
        hosts.add(host);
    }

    public int getNumber(){
        return number;
    }

    public List<String> getHashcodes() {return hashcodes;}

    @Override
    public int compareTo(SimpleImagesInfo iThat) {
        return -Integer.compare(this.getNumber(), iThat.getNumber());
    }
}
