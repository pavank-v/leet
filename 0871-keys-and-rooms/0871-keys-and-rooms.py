class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        visited = set(stack)

        while stack:
            ind = stack.pop()
            for i in rooms[ind]:
                if i not in visited:
                    stack.append(i)
                    visited.add(i)
        return len(rooms) == len(visited)