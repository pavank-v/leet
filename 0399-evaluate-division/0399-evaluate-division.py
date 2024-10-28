class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)

        for i, eq in enumerate(equations):
            a, b = eq
            graph[a].append([b, values[i]])
            graph[b].append([a, 1 / values[i]])
        
        def bfs(src, tar):
            if src not in graph or tar not in graph:
                return -1
            que, visited = deque([[src, 1]]), {src}

            while que:
                n, w = que.popleft()
                if n == tar:
                    return w
                for nei, weight in graph[n]:
                    if nei not in visited:
                        visited.add(nei)
                        que.append([nei, w * weight])
            return -1

        return [bfs(src, tar) for src, tar in queries]
