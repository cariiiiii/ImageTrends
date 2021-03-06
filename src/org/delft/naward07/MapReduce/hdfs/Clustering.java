package org.delft.naward07.MapReduce.hdfs;

import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.security.UserGroupInformation;

/**
 * Main entry for the basic clustering, running on HDFS.
 *
 * @author Feng Wang
 */
public class Clustering implements Runnable {
	private String path;
    private String intermediatePath;
    private String outPath;

    /**
     * Constructor.
     */
	public Clustering(String path, String intermediatePath, String outPath) {
		this.path = path;
        this.intermediatePath = intermediatePath;
        this.outPath = outPath;
	}

	@Override
	public void run() {
        // All configuration......
        // PropertyConfigurator.configure("log4jconfig.properties");
		final Configuration conf = new Configuration();
		// The core-site.xml and hdfs-site.xml are cluster specific. If you wish to use this on other clusters adapt the files as needed.
		conf.addResource(Clustering.class.getResourceAsStream("/nl/surfsara/warcexamples/hdfs/resources/core-site.xml"));
		conf.addResource(Clustering.class.getResourceAsStream("/nl/surfsara/warcexamples/hdfs/resources/hdfs-site.xml"));

		conf.set("hadoop.security.authentication", "kerberos");
		conf.set("hadoop.security.authorization", "true");

		System.setProperty("java.security.krb5.realm", "CUA.SURFSARA.NL");
		System.setProperty("java.security.krb5.kdc", "kdc.hathi.surfsara.nl");

		UserGroupInformation.setConfiguration(conf);

		UserGroupInformation loginUser;

		try {
			loginUser = UserGroupInformation.getLoginUser();
			System.out.println("Logged in as: " + loginUser.getUserName());

            SplitMapOutput splitMapOutput = new SplitMapOutput(conf, path, intermediatePath);
            loginUser.doAs(splitMapOutput);

            RunClustering runClustering = new RunClustering(conf, intermediatePath, outPath);
			loginUser.doAs(runClustering);

		} catch (IOException e) {
			// Just dump the error..
			e.printStackTrace();
		}
	}

}