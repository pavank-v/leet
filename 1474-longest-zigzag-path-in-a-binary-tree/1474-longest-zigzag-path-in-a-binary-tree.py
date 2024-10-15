# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return max(self.traverse(root.left, True, 0), self.traverse(root.right, False, 0))
    
    def traverse(self, root, isLeft, depth):
        if not root:
            return depth
        
        if isLeft:
            depth = max(self.traverse(root.right, False, depth + 1), 
            self.traverse(root.left, True, 0))
        
        else:
            depth = max(self.traverse(root.left, True, depth + 1), 
            self.traverse(root.right, False, 0))
        
        return depth