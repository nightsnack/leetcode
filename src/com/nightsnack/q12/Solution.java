package com.nightsnack.q12;

import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class Solution {

    public String intToRoman(int num) {
        Map<String, String> num2rom = new HashMap<String, String>() {{
            put("1000", "M");
            put("900", "CM");
            put("500", "D");
            put("400", "CD");
            put("100", "C");
            put("90", "XC");
            put("50", "L");
            put("40", "XL");
            put("10", "X");
            put("9", "IX");
            put("5", "V");
            put("4", "IV");
            put("1", "I");
        }};
        String str = num + "";
        int i = str.length();
        StringBuilder rom = new StringBuilder();

        while (i > 0) {
            int count0 = str.length() - i;
            int digit = Character.getNumericValue(str.charAt(i - 1));
            i--;
            String copy0 = String.join("", Collections.nCopies(count0, "0"));

            if (digit % 9 == 0 && digit / 9 == 1) {
                rom.insert(0, num2rom.get("9" + copy0));
                continue;
            }
            if (digit / 4 == 1 && digit % 4 == 0) {
                rom.insert(0, num2rom.get("4" + copy0));
                continue;
            }
            StringBuilder fiveone = new StringBuilder();
            int s = digit / 5;
            int y = digit % 5;
            if (s > 0) {
                fiveone.append(num2rom.get("5" + copy0));
            }
            digit = y;
            for (int j = 0; j < digit; j++) {
                fiveone.append(num2rom.get("1" + copy0));
            }
            rom.insert(0,fiveone);
        }
        return rom.toString();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        String r = s.intToRoman(1997);
        System.out.println(r);
    }

}
