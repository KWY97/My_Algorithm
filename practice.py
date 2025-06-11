N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 체스 말 정보: 말 번호 = 인덱스 + 1 (1번 말 -> 0번 인덱스)
pieces = [list(map(int, input().split())) for _ in range(K)]

# 이동 번호: 1 오른쪽, 2 왼쪽, 3 위쪽, 4 아래쪽
# 보드 색상: 0 흰색, 1 빨간색, 2 파란색