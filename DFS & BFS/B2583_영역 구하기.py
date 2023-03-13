# B2583. 영역 구하기
# [백준] https://www.acmicpc.net/problem/2583


import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


# 모눈종이의 가로와 세로의 길이, 직사각형의 좌표 개수
m, n, k = map(int, input().split())

# 직사각형의 좌표
squares = [list(map(int, input().split())) for _ in range(0, k)]

# 모눈종이 생성
boards = [[0] * n for _ in range(0, m)]


# 모눈종이에 직사각형을 그림
for square in squares:
    start_x, start_y, end_x, end_y = square

    for i in range(start_y, end_y):
        for j in range(start_x, end_x):
            boards[i][j] = 1


# 깊이 우선 탐색 알고리즘
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def DFS(x, y):
    global count

    # 영역이 칠해지지 않았으면 영역을 칠 함
    boards[x][y] = 1

    # 영역의 넓이 증가
    count = count + 1

    for i in range(0, 4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and boards[nx][ny] == 0:
            DFS(nx, ny)


answers = []

for i in range(0, m):
    for j in range(0, n):
        # 모눈종이에 칠해지지 않은 영역의 넓이 계산
        if boards[i][j] == 0:
            count = 0

            DFS(i, j)
            answers.append(count)


print(len(answers))

for answer in sorted(answers):
    print(answer, end=" ")
