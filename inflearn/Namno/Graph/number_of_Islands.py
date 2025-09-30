class Solution(object):
    def numIslands(self, grid):
        def dfs(x, y):
            visited[x][y] = 1

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if visited[nx][ny] == 1:
                    continue
                if grid[nx][ny] == '0':
                    continue
                dfs(nx, ny)

        m = len(grid)
        n = len(grid[0])

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        visited = [[0] * n for _ in range(m)]

        cnt = 0

        for i in range(m):
            for j in range(n):
                if (grid[i][j] == '1') and (visited[i][j] == 0):
                    dfs(i, j)
                    cnt += 1
        return cnt