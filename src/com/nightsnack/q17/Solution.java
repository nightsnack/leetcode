package com.nightsnack.q17;

import java.util.*;

public class Solution {
    Map<String, String[]> phone = new HashMap<String, String[]>() {{
        put("2", new String[]{"a","b","c"});
        put("3", new String[]{"d","e","f"});
        put("4", new String[]{"g","h","i"});
        put("5", new String[]{"j","k","l"});
        put("6", new String[]{"m","n","o"});
        put("7", new String[]{"p","q","r", "s"});
        put("8", new String[]{"t","u","v"});
        put("9", new String[]{"w","x","y", "z"});
    }};

    public void recurFind( String[] numstr, String pref, List<String> res) {
        if (numstr.length == 0) {
            res.add(pref);
            return;
        }

        String[] strarr = phone.get(numstr[0]);
        for (int i = 0; i < strarr.length; i++) {
            String npref = pref+strarr[i];
            recurFind(Arrays.copyOfRange(numstr, 1, numstr.length), npref, res);
        }
    }

    public List<String> letterCombinations(String digits) {
        String[] numstr = digits.split("");
        if (digits.equals(""))
            return new ArrayList<>();
        List<String> res = new ArrayList();
        recurFind(numstr,"", res );
        return res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        List<String> res = s.letterCombinations("");
        res.forEach(System.out::println);
    }
}
