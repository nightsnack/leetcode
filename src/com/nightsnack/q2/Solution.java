package com.nightsnack.q2;




/**
 * You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

 You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 Example

 Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 Output: 7 -> 0 -> 8
 Explanation: 342 + 465 = 807.

 */
class Solution {

    public static void main(String[] args) {
        Solution s = new Solution();
        ListNode l1 = new ListNode(7);
        ListNode l12 = new ListNode(8);
        l1.next = l12;
        ListNode l13 = new ListNode(9);
        l12.next = l13;
        ListNode l2 = new ListNode(3);
        ListNode l21 = new ListNode(1);
        l2.next = l21;
//        ListNode l22 = new ListNode(4);
//        l21.next = l22;
        ListNode l3 = s.addTwoNumbers(l1,l2);
        System.out.println("l3");
    }


    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if (l1 == null) return l2;
        if (l2 == null) return l1;
        ListNode firstnode = new ListNode(0);
        boolean carry_sym = false;
        ListNode currentnode = firstnode;

        int a,b;
        do {

            a = (l1!=null)? l1.val:0;
            b = (l2!=null)? l2.val:0;
            int c = (carry_sym == true)?1:0;
            int val = a + b + c;
            carry_sym = false;

            if (val >= 10)
            {
                carry_sym = true;
                val -= 10;
            }

            currentnode.next = new ListNode(val);
            currentnode = currentnode.next;
            if (l2!=null) l2 = l2.next;
            if (l1!=null) l1 = l1.next;
        }
        while (l1!= null || l2!= null);

        if (carry_sym)
            currentnode.next = new ListNode(1);

        return firstnode.next;
    }
}