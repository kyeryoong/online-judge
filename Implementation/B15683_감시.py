# B14503. 감시
# [백준] https://www.acmicpc.net/problem/14503


from itertools import product
from copy import deepcopy

import sys
input = sys.stdin.readline


# 사무실의 크기
n, m = list(map(int, input().split()))

boards = [list(map(int, input().split())) for _ in range(0, n)]


# CCTV의 위치
cameras = []

for i in range(0, n):
    for j in range(0, m):
        if 0 < boards[i][j] < 6:
            cameras.append((i, j, boards[i][j]))


# 각 CCTV 방향 경우의 수
directions = list(product(["L", "R", "U", "D"], repeat=len(cameras)))


answer = int(1e9)


# 왼쪽 감시 함수
def left(x, y):
    global new_boards

    for k in range(y - 1, -1, -1):
        if new_boards[x][k] == 6:
            break

        if new_boards[x][k] == 0:
            new_boards[x][k] = 9


# 오른쪽 감시 함수
def right(x, y):
    global new_boards

    for k in range(y + 1, m):
        if new_boards[x][k] == 6:
            break

        if new_boards[x][k] == 0:
            new_boards[x][k] = 9


# 위쪽 감시 함수
def up(x, y):
    global new_boards

    for k in range(x - 1, -1, -1):
        if new_boards[k][y] == 6:
            break

        if new_boards[k][y] == 0:
            new_boards[k][y] = 9


# 아래쪽 감시 함수
def down(x, y):
    global new_boards

    for k in range(x + 1, n):
        if new_boards[k][y] == 6:
            break

        if new_boards[k][y] == 0:
            new_boards[k][y] = 9


# 모든 CCTV 방향 경우의 수에 대해서 시뮬레이션 수행
for i in range(0, len(directions)):
    # 사각 지대 개수
    count = 0

    new_boards = deepcopy(boards)

    for j in range(0, len(cameras)):
        # CCTV의 위치와 CCTV 종류
        x, y, camera_type = cameras[j]
        
        # 해당 CCTV의 방향
        direction = directions[i][j]


        # 1번 CCTV인 경우
        if camera_type == 1:
            if direction == "L":
                left(x, y)

            elif direction == "R":
                right(x, y)

            elif direction == "U":
                up(x, y)

            elif direction == "D":
                down(x, y)

        # 2번 CCTV인 경우
        elif camera_type == 2:
            if direction == "L" or direction == "R":
                left(x, y)
                right(x, y)

            elif direction == "U" or direction == "D":
                up(x, y)
                down(x, y)

        # 3번 CCTV인 경우
        elif camera_type == 3:
            if direction == "L":
                left(x, y)
                up(x, y)

            elif direction == "U":
                up(x, y)
                right(x, y)

            elif direction == "R":
                right(x, y)
                down(x, y)

            elif direction == "D":
                down(x, y)
                left(x, y)

        # 4번 CCTV인 경우
        elif camera_type == 4:
            if direction == "L":
                down(x, y)
                left(x, y)
                up(x, y)

            elif direction == "U":
                left(x, y)
                up(x, y)
                right(x, y)

            elif direction == "R":
                up(x, y)
                right(x, y)
                down(x, y)

            elif direction == "D":
                right(x, y)
                down(x, y)
                left(x, y)

        # 5번 CCTV인 경우
        elif camera_type == 5:
            left(x, y)
            right(x, y)
            up(x, y)
            down(x, y)


    # 사각 지대 계산
    for i in range(0, n):
        for j in range(0, m):
            if new_boards[i][j] == 0:
                count = count + 1


    answer = min(answer, count)


print(answer)
