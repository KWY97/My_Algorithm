def stack_arr(n, arr):
    stack = []
    num = 1
    arr_idx = 0
    result = []

    while True:
        if not stack:
            stack.append(num)
            result.append('+')
            num += 1

        elif arr[arr_idx] == stack[-1]:
            stack.pop()
            result.append('-')
            arr_idx += 1

            if arr_idx == n:
                break
        else:
            if n < num:
                return "NO"
                break

            stack.append(num)
            result.append('+')
            num += 1
    return result

arr = []
n = int(input())
for _ in range(n):
    arr.append(int(input()))

ans = stack_arr(n, arr)

if ans == "NO":
    print(ans)
else:
    for x in ans:
        print(x)