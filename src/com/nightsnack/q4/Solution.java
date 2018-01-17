package com.nightsnack.q4;


import java.util.ArrayList;
import java.util.List;

/**
 * There are two sorted arrays nums1 and nums2 of size m and n respectively.
 * <p>
 * Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
 * <p>
 * Example 1:
 * nums1 = [1, 3]
 * nums2 = [2]
 * <p>
 * The median is 2.0
 * Example 2:
 * nums1 = [1, 2]
 * nums2 = [3, 4]
 * <p>
 * The median is (2 + 3)/2 = 2.5
 */
class Solution {

    public static void main(String[] args) {
        int[] nums1 = {1, 3};
        int[] nums2 = {2};
        int[] nums11 = {1, 2};
        int[] nums21 = {3, 4};
        Solution s = new Solution();
        System.out.println(s.findMedianSortedArrays(nums1, nums2));
        System.out.println(s.findMedianSortedArrays(nums11, nums21));
    }

    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int i = 0, j = 0;
        double res;
        List<Integer> seq = new ArrayList<>();
        int a,b;
        while (i != nums1.length || j != nums2.length) {
            a = (i == nums1.length) ?327688888:nums1[i];
            b = (j == nums2.length) ?327688888:nums2[j];

            if (a <= b) {
                seq.add(a);
                i++;
            } else {
                seq.add(b);
                j++;
            }
        }

        if (seq.size()%2 == 0) {
            res = ( seq.get(seq.size()/2) + seq.get(seq.size()/2-1) ) / 2.0;
        } else {
            res = seq.get(seq.size()/2);
        }
        return res;

    }

}