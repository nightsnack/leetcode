package test.ctve;

import java.util.Scanner;

public class Main1 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        while (in.hasNext()) {
            String accountA = in.next();
            String accountB = in.next();
            int add = 1;
            int delete = 1;
            int update = 1;
            int cost = calculate(accountA, accountB, add, delete, update);
            System.out.println("亲密度为:" + cost);
        }
        in.close();
    }

    private static int calculate(String accountA, String accountB, int add, int delete, int update) {
        int len1 = accountA.length();
        int len2 = accountB.length();
        int[][] dif = new int[len1 + 1][len2 + 1];

        for (int a = 0; a <= len1; a++) {
            dif[a][0] = a;
        }
        for (int a = 0; a <= len2; a++) {
            dif[0][a] = a;
        }
        int temp;
        for (int i = 1; i <= len1; i++) {
            for (int j = 1; j <= len2; j++) {
                if (accountA.charAt(i - 1) == accountB.charAt(j - 1)) {
                    temp = 0;
                } else {
                    temp = update;
                }
                dif[i][j] = min(dif[i - 1][j - 1] + temp, dif[i][j - 1] + add,
                        dif[i - 1][j] + delete);
            }
        }

        //计算相似度
        int similarity =(int) (1 - (float) dif[len1][len2] / Math.max(accountA.length(), accountB.length()));

        return similarity;
    }

    private static int min(int... is) {
        int min = Integer.MAX_VALUE;
        for (int i : is) {
            if (min > i) {
                min = i;
            }
        }
        return min;
    }
}