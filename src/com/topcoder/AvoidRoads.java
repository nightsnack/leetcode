package com.topcoder;

import java.util.HashMap;
import java.util.Map;

/** Dynamic Programming
 * https://community.topcoder.com/stat?c=problem_statement&pm=1889&rd=4709
 */
public class AvoidRoads {
    public static void main(String[] args) {
        String[] bad = {"0 0 0 1", "6 6 5 6"};
//        String[] bad = {"0 0 0 1", "6 6 5 6"};
//        String[] bad = {"0 0 1 0", "1 2 2 2", "1 1 2 1"};
        long p = numWays(6, 6, bad);
        System.out.printf(p + ""); //should be 252
    }

    public static long numWays(int weight, int height, String[] bad) {
        Map<String, String> badmap = new HashMap<>();
        for (int i = 0; i < bad.length; i++) {
            String[] point = bad[i].split(" ");
            int k1 = point[0].charAt(0) + point[1].charAt(0), k2 = point[2].charAt(0) + point[3].charAt(0);
            String key = k1 > k2 ? point[0] + point[1] : point[2] + point[3];     // pick up the largest of the bad (destnation) as the key
            String value = k1 < k2 ? point[0] + point[1] : point[2] + point[3];   // pick up the smallest of the bad (destnation) as the value
            badmap.put(key, value);
        }
        long[][] paths = new long[weight+1][height+1];
        for (int i = 0; i < weight+1; i++) {
            for (int j = 0; j < height+1; j++) {
                long x = 0, y = 0;
                if (i > 0 && (!badmap.containsKey(String.valueOf(i) + String.valueOf(j)) || !badmap.get(String.valueOf(i) + String.valueOf(j)).equals(String.valueOf(i - 1) + String.valueOf(j)))) {
                    int t = 0;
                    if (i == 1 && j == 0) {
                        t = 1;
                    }
                    x = paths[i - 1][j] + t;
                }

                if (j > 0 && (!badmap.containsKey(String.valueOf(i) + String.valueOf(j)) || !badmap.get(String.valueOf(i) + String.valueOf(j)).equals(String.valueOf(i) + String.valueOf(j - 1)))) {
                    int t = 0;
                    if (j == 1 && i == 0)
                        t = 1;
                    y = paths[i][j - 1] + t;
                }

                paths[i][j] = x + y;
            }
        }

        return paths[weight][height];
    }
}
