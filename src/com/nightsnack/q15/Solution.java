package com.nightsnack.q15;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
/**
 * 三个游标请务必记得选定左边第一个开始循环，而不是选定中间那个，选中间那个会出现无法去重的问题，要么少要么多。
 * Time: O(n2)
 * Space: O(1)
 */

public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        if (nums.length < 3) return new ArrayList<>();
        Arrays.sort(nums);
        List<List<Integer>> resList = new ArrayList<>();
        for (int i = 0; i < nums.length - 2; i++) {
            if (i>0 && nums[i] == nums[i-1])
                continue;
            int j = i+1, k = nums.length - 1;
            while (j < k ) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum == 0) {
                    resList.add(Arrays.asList(nums[j], nums[i], nums[k]));
                }
                if (sum <= 0) {
                    do
                        j++;

                    while (nums[j] == nums[j - 1] && j < i);
                }
                if (sum >= 0) {
                    do
                        k--;

                    while (nums[k] == nums[k + 1] && k > i);
                }
            }
        }
        return resList;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = new int[]{-1, 0, 1, 2, -1, -4};
        List res = s.threeSum(nums);
        res.forEach(System.out::println);
    }

}
