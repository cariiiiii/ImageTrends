package org.delft.naward07.postProcessing;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;

/**
 * Some post processing function for PHP.
 *
 * Created by wdwind on 14-8-30.
 */

public class FilesForPHP {

    /**
     * For every file in the input folder, extract its name. (Because the file is the output of the
     * Map process, it has a specific format, yyyymm, for example, 200103).
     * This function record the name and generate another format, for example, Mar. 2001. And generate
     * PHP array format output.
     *
     * @param inputFolder Input folder, which contains the outputs of the Map.
     * @param outputName Output file.
     * @throws IOException
     */
    public static void getTimePeriodsName(String inputFolder, String outputName) throws IOException {
        File f = new File(inputFolder);
        //ArrayList<File> files = new ArrayList<File>(Arrays.asList(f.listFiles()));
        ArrayList<String> names = new ArrayList<String>(Arrays.asList(f.list()));

//        for(File ff: files)
//            System.out.println(ff.getParent());

        System.out.println("----------------------------");

        for(String n: names)
            System.out.println(n);

        BufferedWriter bw = new BufferedWriter(new FileWriter(new File(outputName)));

        for(String n: names){
            try {
                Integer.parseInt(n);
//                Integer year = Integer.parseInt(n.substring(0, 4));
//                Integer month = Integer.parseInt(n.substring(4, 6));

                String year = n.substring(0, 4);
                String month = n.substring(4, 6);

                StringBuilder sb = new StringBuilder();
                sb.append("\"");
                sb.append(n);
                sb.append("\"");
                sb.append(", ");
                bw.write(sb.toString());

                System.out.println(year);
                System.out.println(month);

            } catch (Exception e){
                //e.printStackTrace();
                continue;
            }
        }

        bw.write("\n");

        for(String n: names){
            try {
                Integer.parseInt(n);
//                Integer year = Integer.parseInt(n.substring(0, 4));
                Integer month = Integer.parseInt(n.substring(4, 6));

                String year = n.substring(0, 4);
//                String month = n.substring(4, 6);

                String mon = getMon(month);

                StringBuilder sb = new StringBuilder();
                sb.append("\"");
                sb.append(mon);
                sb.append(" ");
                sb.append(year);
                sb.append("\"");
                sb.append(", ");
                bw.write(sb.toString());

                System.out.println(year);
                System.out.println(month);

            } catch (Exception e){
                //e.printStackTrace();
                continue;
            }
        }

        bw.flush();
        bw.close();
    }

    /**
     * Corresponding between number of month and the abbreviation of the month.
     *
     * @param month Month in number, ie. 01 represents January.
     * @return Month in String abbreviation, ie. Jan.
     */
    private static String getMon(int month) {
        switch (month){
            case 1:
                return "Jan.";
            case 2:
                return "Feb.";
            case 3:
                return "Mar.";
            case 4:
                return "Apr.";
            case 5:
                return "May.";
            case 6:
                return "Jun.";
            case 7:
                return "Jul.";
            case 8:
                return "Aug.";
            case 9:
                return "Sep.";
            case 10:
                return "Oct.";
            case 11:
                return "Nov.";
            case 12:
                return "Dec";
            default:
                return "";
        }

    }

    /**
     * Calculate the number of all images gathered.
     *
     * @param inputFolder The output folder of Map (org.delft.naward07.MapReduce.hdfs.SplitMapOutput).
     */
    public static void totalLines(String inputFolder){
        long lines = 0;

        File f = new File(inputFolder);
        ArrayList<File> files = new ArrayList<File>(Arrays.asList(f.listFiles()));
        ArrayList<String> names = new ArrayList<String>(Arrays.asList(f.list()));

        System.out.println("----------------------------");

        for(String n: names)
            System.out.println(n);

        int i = 0;
        for(String n: names){
            try {
                Integer.parseInt(n);

                System.out.println(files.get(i).getAbsolutePath());

                lines += countLines(files.get(i).getAbsolutePath());

            } catch (Exception e){
                //e.printStackTrace();
                //continue;
            }
            i++;
        }

        System.out.println(lines);
    }

    /**
     * Count lines of one file.
     *
     * @param filename File String.
     * @return Number of lines in the file.
     * @throws IOException
     */
    public static long countLines(String filename) throws IOException {
        InputStream is = new BufferedInputStream(new FileInputStream(filename));
        try {
            byte[] c = new byte[1024];
            long count = 0;
            int readChars = 0;
            boolean empty = true;
            while ((readChars = is.read(c)) != -1) {
                empty = false;
                for (int i = 0; i < readChars; ++i) {
                    if (c[i] == '\n') {
                        ++count;
                    }
                }
            }
            return (count == 0 && !empty) ? 1 : count;
        } finally {
            is.close();
        }
    }

    /**
     * Get the number of images in each file (month), and output to PHP array format.
     *
     * @param inputFolder Input folder path, which contains the outputs of the Map.s
     */
    public static void getImgNum(String inputFolder){
        File f = new File(inputFolder);
        ArrayList<File> files = new ArrayList<File>(Arrays.asList(f.listFiles()));
        ArrayList<String> names = new ArrayList<String>(Arrays.asList(f.list()));

        StringBuilder sb = new StringBuilder();
        sb.append("array(");

        int i = 0;
        for(String n: names){
            try {
                Integer.parseInt(n);

                System.out.println(files.get(i).getAbsolutePath());

                sb.append("\"");
                sb.append(n);
                sb.append("\"=>\"");
                sb.append(countLines(files.get(i).getAbsolutePath()));
                sb.append("\",");
            } catch (Exception e){
                //e.printStackTrace();
                //continue;
            }
            i++;
        }
        sb.append(");");

        System.out.println(sb.toString());
    }

    /**
     * Get top N lines of every file in the input folder, and the output to the output folder.
     *
     * @param inputFolder Input folder path, which contains the outputs of the Map.
     * @param outputFolder Output folder path.
     * @param N Top N lines want to preserve.
     */
    public static void getNLines(String inputFolder, String outputFolder, int N){
        File f = new File(inputFolder);
        ArrayList<File> files = new ArrayList<File>(Arrays.asList(f.listFiles()));
        ArrayList<String> names = new ArrayList<String>(Arrays.asList(f.list()));

        int i = 0;
        for(String n: names){
            try {
                //Integer.parseInt(n);

                System.out.println(files.get(i).getAbsolutePath());

                BufferedReader br = new BufferedReader(new FileReader(files.get(i).getAbsoluteFile()));
                BufferedWriter bw = new BufferedWriter(new FileWriter(new File(outputFolder + "\\" + n)));

                int num = 0;
                String line = br.readLine();

                while (line != null){
                    bw.write(line);
                    bw.write("\n");

                    if(num >= N){
                        break;
                    }

                    num ++;
                    line = br.readLine();
                }

                br.close();
                bw.flush();
                bw.close();

            } catch (Exception e){
                e.printStackTrace();
                //continue;
            }
            i++;
        }
    }

    public static void main(String[] args) throws IOException {
        //FilesForPHP.getTimePeriodsName("C:\\Users\\wdwind\\SkyDrive\\文档\\clustering008", "C:\\Users\\wdwind\\SkyDrive\\文档\\clustering008\\time");
        //FilesForPHP.totalLines("C:\\Users\\wdwind\\SkyDrive\\文档\\clustering008");
        //FilesForPHP.getImgNum("C:\\Users\\wdwind\\SkyDrive\\文档\\clustering008");
        FilesForPHP.getNLines("C:\\Users\\wdwind\\SkyDrive\\文档\\clustering008\\ranked_clusters\\ranked_clusters", "C:\\Users\\wdwind\\SkyDrive\\文档\\clustering008\\ranked_clusters\\ranked_clusters_top_100", 102);
    }

}
