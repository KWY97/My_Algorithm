# Top Down 방식
class Solution(object):
    def minCostClimbingStairs(self, cost):
        top = len(cost)
        memo = {}

        def dp(n):
            if n == 0 or n == 1:
                return 0

            if n not in memo:
                memo[n] = min(dp(n - 1) + cost[n - 1], dp(n - 2) + cost[n - 2])
            return memo[n]

        return dp(top)


# Bottom Up 방식
class Solution(object):
    def minCostClimbingStairs(self, cost):
        top = len(cost)
        memo = [-1] * (top + 1)
        memo[0] = 0
        memo[1] = 0

        def dp(n):
            for i in range(2, n+1):
                memo[i] = min(memo[i-1] + cost[i-1], memo[i-2] + cost[i-2])
            return memo[n]

        return dp(top)