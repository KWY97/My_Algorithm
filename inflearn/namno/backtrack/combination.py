# nums = [1, 2, 3, 4]의 원소 중 k개를 사용한 조합을 반환하시오
def combination(nums, k):
    result = []
    def backtrack(start, curr):
        if len(curr) == k:
            result.append(curr[:])
            return
        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtrack(i+1, curr)
            curr.pop()


    backtrack(0, [])
    return result


print(combination([1, 2, 3, 4], 2))
