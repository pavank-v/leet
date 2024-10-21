# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        que = deque([root])
        res = []

        while que:
            level_len = len(que)
            curr = []

            for i in range(level_len):
                node = que.popleft()
                curr.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(curr)

        ans = 0

        for i in range(len(res)):
            res[i] = sum(res[i])
        print(res)
        return res.index(max(res)) + 1
        