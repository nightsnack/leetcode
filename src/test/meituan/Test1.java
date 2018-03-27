package test.meituan;

import java.util.Arrays;
import java.util.Scanner;

public class Test1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String b = sc.next();
        
        System.out.println(splitA(a,b));
    }

    private static int splitA (String a, String b) {
//        String[] splitStr = new String[a.length()-b.length()+1];
        int sum = 0;
        for (int i = 0; i < a.length()-b.length()+1; i++) {
            String sub = a.substring(i,i+b.length());
            sum+=calculate(sub,b);
        }
        return sum;
    }

    private static int calculateAA(String accountA, String accountB) {
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
                    temp = 1;
                }
                dif[i][j] = minAA(dif[i - 1][j - 1] + temp, dif[i][j - 1] + 1,
                        dif[i - 1][j] + 1);
            }
        }


        return dif[len1][len2];
    }

    private static int minAA(int... is) {
        int min = Integer.MAX_VALUE;
        for (int i : is) {
            if (min > i) {
                min = i;
            }
        }
        return min;
    }

    static int calculate(String x, String y) {
        if (x.isEmpty()) {
            return y.length();
        }

        if (y.isEmpty()) {
            return x.length();
        }

        int substitution = calculate(x.substring(1), y.substring(1))
                + costOfSubstitution(x.charAt(0), y.charAt(0));
        int insertion = calculate(x, y.substring(1)) + 1;
        int deletion = calculate(x.substring(1), y) + 1;

        return min(substitution, insertion, deletion);
    }

    public static int costOfSubstitution(char a, char b) {
        return a == b ? 0 : 1;
    }

    public static int min(int... numbers) {
        return Arrays.stream(numbers)
                .min().orElse(Integer.MAX_VALUE);
    }
}
