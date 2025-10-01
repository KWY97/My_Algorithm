from collections import deque

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        N = len(rooms)
        visited = [0] * (N)
        q = deque([0])
        visited[0] = 1

        while q:
            cur_room = q.popleft()

            for nxt in rooms[cur_room]:
                if visited[nxt]:
                    continue
                q.append(nxt)
                visited[nxt] = 1

        if 0 in visited:
            return False
        return True