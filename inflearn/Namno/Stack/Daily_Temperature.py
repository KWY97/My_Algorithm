class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        ans = [0] * (n)
        stack = []

        for i, v in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < v:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans