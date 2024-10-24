class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0
        count = 0
        visited = set()

        def dfs(start):
            visited.add(start)
            for end in range(len(isConnected)):
                if isConnected[start][end] and end not in visited:
                    visited.add(end)
                    dfs(end)
        for start in range(len(isConnected)):
            if start not in visited:
                count += 1
                dfs(start)


        return count
