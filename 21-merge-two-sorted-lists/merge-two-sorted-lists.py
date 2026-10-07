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
            # solution = solution.next
            if list1.val <= list2.val:
                solution.next = list1
                list1 = list1.next
                solution = solution.next
            else:
                solution.next = list2
                list2 = list2.next
                solution = solution.next

        leftOver = list1 if list1 else list2
        while leftOver:
            solution.next = leftOver
            leftOver = leftOver.next
            solution = solution.next
        
        return temp.next
                

        