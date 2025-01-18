N = int(input())
arr = []
for _ in range(N):
    in_num = int(input())
    arr.append(in_num)
arr.sort()

for num in arr:
    print(num)