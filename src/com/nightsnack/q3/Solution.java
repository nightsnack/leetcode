package com.nightsnack.q3;


import java.util.LinkedList;
import java.util.Queue;

/**
 * Given a string, find the length of the longest substring without repeating characters.
 * <p>
 * Examples:
 * <p>
 * Given "abcabcbb", the answer is "abc", which the length is 3.
 * <p>
 * Given "bbbbb", the answer is "b", with the length of 1.
 * <p>
 * Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
 */
class Solution {

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.lengthOfLongestSubstring("abcabcbb"));
        System.out.println(s.lengthOfLongestSubstring("bbbbbb"));
        System.out.println(s.lengthOfLongestSubstring("pwwkew"));

    }

    public int lengthOfLongestSubstring(String s) {
        char[] c = s.toCharArray();
        Queue<Character> charQueue = new LinkedList<>();
        int lenth = 0;
        for (int i = 0; i < c.length; i++) {
            if (charQueue.contains(c[i]))
                while (charQueue.poll() != c[i]) ;
            charQueue.add(c[i]);
            lenth = Math.max(charQueue.size(), lenth);
        }
        return lenth;
    }

}