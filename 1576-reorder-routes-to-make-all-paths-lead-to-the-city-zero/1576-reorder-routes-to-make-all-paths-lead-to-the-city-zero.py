class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(a, b) for a, b in connections}
        neighbors = {a: [] for a in range(n)}
        visited = set()
        self.count = 0

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        def dfs(start):
            nonlocal edges, neighbors, visited

            for neighbor in neighbors[start]:
                if neighbor in visited:
                    continue
                if (neighbor, start) not in edges:
                    self.count += 1
                visited.add(neighbor)
                dfs(neighbor)
        visited.add(0)
        dfs(0)
        return self.count
        

