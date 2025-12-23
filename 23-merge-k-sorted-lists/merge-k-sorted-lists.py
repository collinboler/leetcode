# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))
        
        # Create dummy head for result list
        dummy = ListNode(0)
        current = dummy
        
        # Process nodes until heap is empty
        while heap:
            # Pop the smallest node from heap
            val, list_idx, node = heapq.heappop(heap)
            
            # Add this node to result list
            current.next = node
            current = current.next
            
            # If this list has more nodes, add the next node to heap
            if node.next:
                heapq.heappush(heap, (node.next.val, list_idx, node.next))
        
        # Return the merged list (skip dummy head)
        return dummy.next




        