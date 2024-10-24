class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(rooms, ind, visited):
            visited.add(ind)
            for i in rooms[ind]:
                if i not in visited:
                    dfs(rooms, i, visited)
        
        dfs(rooms, 0, visited)
        return len(rooms) == len(visited)