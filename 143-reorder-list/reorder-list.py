# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, curr):
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        rev = self.reverse(second)

        first = head

        # head = 1 2
        # rev = 4 3
        while rev:
            # 3
            revNext = rev.next
            # 4
            headNext = head.next
            # 1 -> 4

            rev.next = headNext
            head.next = rev
            
            head = headNext
            rev = revNext
        return first
            
        return firstHead
    
        