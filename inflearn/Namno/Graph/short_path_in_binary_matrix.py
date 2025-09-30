from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])

        def bfs(in_x, in_y):
            visited[in_x][in_y] = 1
            q = deque()
            q.append([in_x, in_y])

            while q:
                x, y = q.popleft()

                if x == end_x and y == end_y:
                    return

                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    if visited[nx][ny] != -1:
                        continue
                    if grid[nx][ny] == 1:
                        continue

                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])


        start_x, start_y = 0, 0
        end_x, end_y = n-1, m-1

        dx = [1, 1, 0, -1, -1, -1, 0, 1]
        dy = [0, 1, 1, 1, 0, -1, -1, -1]
        visited = [[-1] * m for _ in range(n)]

        if grid[start_x][start_y] == 0:
            bfs(start_x, start_y)
        return visited[end_x][end_y]