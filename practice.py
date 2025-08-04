import sys
input = sys.stdin.readline

N, K = map(int, input().split())

diff = []
for _ in range(N):
    A, B = map(int, input().split())
    diff.append(B - A)

diff.sort()

answer = diff[K-1]

if answer < 0:
    answer = 0

print(answer)