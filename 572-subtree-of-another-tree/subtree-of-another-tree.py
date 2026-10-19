# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root):
        if root is None:
            return "#"
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        return "." + str(root.val) + left + right + "."

    def isSubtree(self, root, subRoot):
        return self.dfs(subRoot) in self.dfs(root)
        