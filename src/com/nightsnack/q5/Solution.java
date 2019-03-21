package com.nightsnack.q5;

import java.util.Scanner;

public class Solution {
    public static String longestPalindrome(String s) {
        if (s.length() == 0)
            return s;
        boolean[][] dp = new boolean[s.length()][s.length()];
        String lpd = ""+s.charAt(0);
        int n = s.length();
        for (int i = n-1; i >=0 ; i--) {
            dp[i][i] = true;
            for (int j = i+1; j<n ; j++) {
                if(s.charAt(i) == s.charAt(j) && (dp[i+1][j-1]|| j-i<3))
                {
                    dp[i][j] = true;
                    if (j-i+1>lpd.length())
                        lpd = s.substring(i,j+1);
                }
            }
        }
        return lpd;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str = "aaabca";
        System.out.println(longestPalindrome(str));
    }
}
