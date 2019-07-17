class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        prev = None
        curr = head

        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
