# Top Down 방식
class Solution(object):
    def uniquePaths(self, m, n):
        memo = [[-1] * n for _ in range(m)]

        def dfs(r, c):
            if r == 0 and c == 0:
                memo[r][c] = 1
                return memo[r][c]

            cnt = 0
            if memo[r][c] == -1:
                if r-1 >= 0:
                    cnt += dfs(r-1, c)
                if c-1 >= 0:
                    cnt += dfs(r, c-1)
                memo[r][c] = cnt

            return memo[r][c]
        return dfs(m-1, n-1)


# Bottom Up 방식
class Solution(object):
    def uniquePaths(self, m, n):
        memo = [[-1] * n for _ in range(m)]

        for r in range(m):
            memo[r][0] = 1

        for c in range(n):
            memo[0][c] = 1

        for r in range(1, m):
            for c in range(1, n):
                memo[r][c] = memo[r-1][c] + memo[r][c-1]
        return memo[m-1][n-1]