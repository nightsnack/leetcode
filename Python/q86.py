from Python.q0ListNode import ListNode, stringToListNode, prettyPrintLinkedList


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        dummy = ListNode(val=0, next=head)
        pre = dummy
        curr = pre.next

        while curr:
            if curr.val < x:
                pre = curr
                curr = curr.next
            else:
                break
        slot = pre
        while curr:
            if curr.val< x:
                pre.next = curr.next
                curr.next = slot.next
                slot.next = curr
                slot = curr
                curr = pre.next
            else:
                pre = curr
                curr = curr.next
        return dummy.next

s = Solution()
head = '[1,4,3,2,5,2]'
head = '[2,1]'
head = stringToListNode(head)
x = 3
newhead = s.partition(head, 2)
prettyPrintLinkedList(newhead)
exit(0)
