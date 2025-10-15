# nums = [1, 2, 3, 4]의 모든 부분집합을 반환하시오
def subset(nums, k):
    result = []
    def backtrack(start, curr):
        if len(curr) == k:
            result.append(curr[:])
            return
        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtrack(i+1, curr)
            curr.pop()
    for k in range(len(nums)+1):
        backtrack(0, [])
    return result


print(subset([1, 2, 3, 4], 2))
