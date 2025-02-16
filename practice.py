# 깃 심기용 (프로젝트 때문에 너무너무 바빴다 .. 깃랩에 수도 없이 커밋함)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
for i in arr:
    print(i[0], i[1])
