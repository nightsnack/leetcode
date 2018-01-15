package com.nightsnack.q1;

import java.util.Arrays;

/**
 * Given an array of integers, return indices of the two numbers such that they add up to a specific target.

 You may assume that each input would have exactly one solution, and you may not use the same element twice.

 Example:
 Given nums = [2, 7, 11, 15], target = 9,

 Because nums[0] + nums[1] = 2 + 7 = 9,
 return [0, 1].

 */
public class Solution {
    public static void main(String[] args) {
        int[] nums = {2, 7, 3, 6};
        int target = 9;
        Solution solution = new Solution();
        solution.twoSum(nums, target);
        System.out.println(Arrays.toString(solution.twoSum(nums, target)));
    }

    public int[] twoSum(int[] nums, int target) {
        int[] solution = new int[2];
        a:for (int i = 0; i < nums.length; i++) {
            int rest = target - nums[i];
            for (int j = i+1; j < nums.length; j++) {
                if (rest == nums[j]) {
                    solution[0] = i; solution[1] = j;
                    break a;
                }
            }
        }
        return solution;

    }
}