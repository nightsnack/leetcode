package com.nightsnack.q18_4Sum;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        int N = 4;
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        nsum(nums, target, 0, res, N);
        return res;
    }

    public void nsum(int nums[], int target, int head, List<List<Integer>> res, int n) {
        if (n > 2) {
            for (int i = head; i < nums.length; i++) {
                if (i > head && nums[i] == nums[i - 1]) continue;
                nsum(nums, target - nums[i], i + 1, res, n - 1);
                for (List<Integer> item : res) if (item.size() == n - 1) item.add(nums[i]);

            }
        } else
            simple2sum(nums, target, head, res);
    }

    public void simple2sum(int[] nums, int target, int head, List<List<Integer>> res) {
        int i = head, j = nums.length - 1;
        int oi = i, oj = j;
        while (i < j) {
            if (nums[i] + nums[j] == target) {
                res.add(new ArrayList<>(Arrays.asList(nums[i], nums[j])));
                i++;
                j--;
            } else {
                if (nums[i] + nums[j] >= target)
                    j--;
                else i++;
            }

            while (i > oi && nums[i] == nums[i-1] && i < j) i++;
            while (j < oj && nums[j] == nums[j+1] && i < j) j--;
        }
    }


    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {1, 0, -1, 0, -2, 2};
        List res = s.fourSum(nums, 0);
        res.forEach(System.out::println);
    }
}
