package com.nightsnack.q14;

public class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) return "";
        String prefix = strs[0];
        int mark = prefix.length();
        for (int i = 1; i <strs.length ; i++) {
            if (strs[i].length() == 0)
                return "";
            int j;
            int minLength = Math.min(mark, strs[i].length());
            for (j = 0; j < minLength; j++) {
                if (strs[i].charAt(j) != prefix.charAt(j))
                    break;
            }
            mark = j;
        }
        return prefix.substring(0,mark);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        String[] worlds = new String[] {"aaa","aa","aaa"};
        String pre = s.longestCommonPrefix(worlds);
        System.out.println(pre);
    }
}