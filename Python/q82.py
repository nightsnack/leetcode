from Python.q0ListNode import ListNode, stringToListNode, prettyPrintLinkedList


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(val=0, next=head)
        pre = dummy
        cur = pre.next
        while cur:
            cval = cur.val
            flag = False
            while cur.next and cur.next.val == cval:
                flag = True
                cur = cur.next
            if flag:
                cur = cur.next
                pre.next = cur
            else:
                pre = cur
                cur = cur.next
        return dummy.next

s = Solution()
head = '[1,2,3,3,4,4,5]'
head = stringToListNode(head)
newhead = s.deleteDuplicates(head)
prettyPrintLinkedList(newhead)
exit(0)
