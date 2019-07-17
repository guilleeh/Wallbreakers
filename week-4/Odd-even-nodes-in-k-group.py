# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        odd = head
        even = head.next
        evenHead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = evenHead
        return head


#         odd = []
#         even = []
#         dummy = head
#         index = 1
#         while dummy:
#             if index % 2 == 0:
#                 even.append(dummy.val)
#             else:
#                 odd.append(dummy.val)
#             dummy = dummy.next
#             index += 1

#         if len(odd) == 0 and len(odd) == 0:
#             return head
#         newHead = ListNode(odd.pop(0))
#         dummyNewHead = newHead

#         for i in range(len(odd)):
#             dummyNewHead.next = ListNode(odd[i])
#             dummyNewHead = dummyNewHead.next

#         for i in range(len(even)):
#             dummyNewHead.next = ListNode(even[i])
#             dummyNewHead = dummyNewHead.next

#         return newHead
# Extra space approach

