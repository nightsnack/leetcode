package com.nightsnack.q16;

import java.util.Arrays;

import static java.lang.Math.abs;

public class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int closestsum = nums[0] + nums[1] + nums[nums.length - 1];
        int subvalue = closestsum - target;
        for (int i = 0; i < nums.length - 2; i++) {
            int head = i + 1, tail = nums.length - 1;
            while (head < tail) {
                int diff = nums[i] + nums[head] + nums[tail] - target;
                if (abs(diff) < abs(subvalue)) {
                    subvalue = diff;
                    closestsum = diff+target;
                }
                if (diff > 0)
                    tail--;
                else if (diff < 0)
                    head++;
                else return closestsum;
            }
        }
        return closestsum;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = new int[]{-1, 2, 1, -4};
        int res = s.threeSumClosest(nums,1);
        System.out.println(res);
    }

}
