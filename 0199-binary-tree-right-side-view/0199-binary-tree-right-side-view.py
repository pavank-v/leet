# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        que = deque([root])
        res = []

        while que:
            level_size = len(que)            
            curr = []

            for _ in range(level_size):
                node = que.popleft()
                curr.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(curr)
        
        ans = []

        for arr in res:
            ans.append(arr[-1])
        
        return ans

                