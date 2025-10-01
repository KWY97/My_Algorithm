class Solution(object):
    def twoSum(self, nums, target):
        memo = {}
        for i, v in enumerate(nums):
            needed = target - v
            if needed in memo:
                return [memo[needed], i]
            memo[v] = i

