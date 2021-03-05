from Python.q0ListNode import ListNode, stringToListNode, prettyPrintLinkedList


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if right == 1:
            return head
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        for i in range(1,left):
            pre = pre.next
        curr = pre.next
        for i in range(left, right):
            temp = curr.next
            curr.next = temp.next
            temp.next = pre.next
            pre.next = temp
        return dummy.next

s = Solution()
head = '[1,2,3,4,5]'
head = stringToListNode(head)
left = 2
right = 4

head = '[5]'
head = stringToListNode(head)
left = 1
right = 1
s.reverseBetween(head, left, right)
prettyPrintLinkedList(head)
exit(0)




