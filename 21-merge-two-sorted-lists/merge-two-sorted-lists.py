# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:

        solution = ListNode()

        temp = solution

        while list1 and list2:
            if list1.val <= list2.val:
                solution.next = list1
                list1 = list1.next
            else:
                solution.next = list2
                list2 = list2.next
            solution = solution.next
        left = list1 if list1 else list2
        while left:
            solution.next = left
            left = left.next
            solution = solution.next
        return temp.next

        