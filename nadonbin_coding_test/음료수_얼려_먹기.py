from collections import deque

def bfs(r, c, my_map, visited, n, m):
    queue = deque()
    queue.append([r, c])
    visited[r][c] = True

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            next_r = r + dr[i]
            next_c = c + dc[i]

            if next_r < 0 or next_r >= n or next_c < 0 or next_c >= m:
                continue
            if my_map[next_r][next_c] == 1:
                continue
            if visited[next_r][next_c]:
                continue

            queue.append([next_r, next_c])
            visited[next_r][next_c] = True

N, M = map(int, input().split())
my_map = [list(map(int, input())) for _ in range(N)]
visited = [([False] * M) for _ in range(N)]
cnt = 0
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


for i in range(N):
    for j in range(M):
        if my_map[i][j] == 0 and not visited[i][j]:
            bfs(i, j, my_map, visited, N, M)
            cnt += 1
print(cnt)