# B16927. 배열 돌리기 2
# [백준] https://www.acmicpc.net/problem/16927


import sys
input = sys.stdin.readline


# 배열의 크기와, 회전 횟수
n, m, r = map(int, input().split())

# 배열
arrays = [list(map(int, input().split())) for _ in range(0, n)]


# (a, b) ~ (x, y) 배열의 테두리를 회전
def rotate(a, b, x, y):
    # 가로 또는 세로의 길이가 1이면 회전을 하지 않음
    if a == x or b == y:
        return

    init = arrays[a][b]

    # 위쪽
    for i in range(b, y, 1):
        arrays[a][i] = arrays[a][i + 1]

    # 오른쪽
    for i in range(a, x, 1):
        arrays[i][y] = arrays[i + 1][y]

    # 아래쪽
    for i in range(y, b, - 1):
        arrays[x][i] = arrays[x][i - 1]

    # 왼쪽
    for i in range(x, a, -1):
        arrays[i][b] = arrays[i - 1][b]

    arrays[a + 1][b] = init


# 배열의 깊이
depth = min(n, m) // 2

for i in range(0, depth):
    # 배열 안의 가로와 세로 크기
    size_x = n - i * 2
    size_y = m - i * 2
    
    # [Key Point] 회전 횟수
    # 배열을 일정 횟수 회전하면 초기 상태와 동일함
    cycles = r % ((size_x - 1) * 2 + (size_y - 1) * 2)
    
    for _ in range(0, cycles):
    # 제일 바깥쪽 테두리부터 제일 안쪽 테두리까지 회전 수행
        rotate(i, i, n - i - 1, m - i - 1)


# 회전된 배열 출력
for i in range(0, n):
    for j in range(0, m):
        print(arrays[i][j], end=" ")
    print()
