# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:

        dummy = ListNode(0, head)

        w1 = w2 = dummy
        i = 0
        while i < n + 1:
            i += 1
            w2 = w2.next
        
        
        while w2:
            prev = w1
            w1 = w1.next
            w2 = w2.next
        
        w1.next = w1.next.next


        return dummy.next
        
            
        