# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
         # Create min-heap to track smallest node from each list
        heap = []
        
        # Add first node from each non-empty list to heap
        # Use index to break ties for nodes with same value
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        # Create dummy head for result list
        dummy = ListNode(0)
        current = dummy
        
        # Process heap until empty
        while heap:
            # Extract node with minimum value
            val, i, node = heapq.heappop(heap)
            
            # Add to result list
            current.next = node
            current = current.next
            
            # If extracted node has a next node, add it to heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        # Return merged list (skip dummy head)
        return dummy.next