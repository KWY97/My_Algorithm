arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# 시계 방향 회전 - 방법 1 (정사각형, 직사각형 다 가능)
arr_90 = (list(map(list, zip(*arr[::-1]))))
arr_180 = [a[::-1] for a in arr[::-1]]
arr_270 = [x[::-1] for x in (list(map(list, zip(*arr[::-1]))))[::-1]]

# 시계 방향 회전 - 방법 2 (정사각형 버전)
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = 3

new_90 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_90[j][n-i-1] = arr[i][j]

new_180 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_180[n-i-1][n-j-1] = arr[i][j]

new_270 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_270[n-j-1][i] = arr[i][j]

# 시계 방향 회전 - 방법 2 (직사각형 버전)
def rotate_90(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

def rotate_180(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * m for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[n-i-1][m-j-1] = a[i][j]

def rotate_270(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(m):
            result[m-j-1][i] = a[i][j]
    return result
