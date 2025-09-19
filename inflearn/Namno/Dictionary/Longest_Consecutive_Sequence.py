# 내 풀이
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        nums = sorted(list(nums))

        n = len(nums)
        ans = 0
        idx = 0
        cnt = 1

        if not nums:
            return 0

        while idx < n - 1:
            if nums[idx] + 1 == nums[idx + 1]:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 1

            idx += 1

        ans = max(ans, cnt)
        return ans


# 강의 풀이
# 내 풀이
# class Solution(object):
#     def longestConsecutive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         longest = 0
#         num_dict = {}
#
#         for num in nums:
#             num_dict[num] = True
#
#         for num in num_dict:
#             if num - 1 not in num_dict:
#                 cnt = 1
#                 target = num + 1
#
#                 while target in num_dict:
#                     target += 1
#                     cnt += 1
#                 longest = max(longest, cnt)
#         return longest