package com.nightsnack.q13;

import java.util.HashMap;
import java.util.Map;

public class Solution {

    public static Map<String, Integer> rom2digit = new HashMap<String, Integer>() {{
        put("M", 1000);
        put("CM", 900);
        put("D", 500);
        put("CD", 400);
        put("C", 100);
        put("XC", 90);
        put("L", 50);
        put("XL", 40);
        put("X", 10);
        put("IX", 9);
        put("V", 5);
        put("IV", 4);
        put("I", 1);
    }};

    public int romanToInt(String s) {
        int i = s.length();
        int arab = 0;
        while (i>0) {
            String rom = s.substring(i-1, i);
            int value = rom2digit.get(rom);
            if (i!=s.length()) {
                String lastStr = s.substring(i,i+1);
                if (rom2digit.get(lastStr) >value)
                    value = -value;
            }
            arab += value;
            i--;
        }
        return arab;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int num = s.romanToInt("MCMXCIV");
        System.out.println(num);
    }
}
