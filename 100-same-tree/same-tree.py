# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def bfs(self, root):
        result = ""
        if root is None:
            return result
        queue = deque([root])

        while queue:
            node = queue.popleft()
            result += str(node.val)
            if node.left:
                queue.append(node.left)
            else:
                result += "L"
            if node.right:
                queue.append(node.right)
            else:
                result += "R"
        return result
        
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        pR = self.bfs(p)
        qR = self.bfs(q)

        return pR == qR        