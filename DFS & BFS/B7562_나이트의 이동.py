# B7562. 나이트의 이동
# [백준] https://www.acmicpc.net/problem/7562


from collections import deque
import sys
input = sys.stdin.readline


# 나이트의 이동
dx = [-2, -2, 2, 2, -1, -1, 1, 1]
dy = [-1, 1, -1, 1, -2, 2, -2, 2]


for _ in range(0, int(input())):
    size = int(input())  # 체스판의 크기
    start_x, start_y = map(int, input().split())    # 나이트가 현재 있는 칸
    finish_x, finish_y = map(int, input().split())  # 나이트가 이동하려고 하는 칸


    # [Key Point] 체스판의 값은 이동 횟수, 초기에는 모두 -1로 초기화
    boards = [[-1 for _ in range(0, size)] for _ in range(0, size)]


    queue = deque()
    queue.append((start_x, start_y))


    # 현재 있는 칸은 이동 횟수를 0으로 초기화
    boards[start_x][start_y] = 0


    # 너비 우선 탐색 알고리즘
    while queue:
        x, y = queue.popleft()

        # [Key Point] 시간 초과 해결을 위해 이동하려고 하는 칸에 도달하면 반복문 종료
        if x == finish_x and y == finish_y:
            break

        for i in range(0, 8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < size and 0 <= ny < size and boards[nx][ny] == -1:
                queue.append((nx, ny))
                boards[nx][ny] = boards[x][y] + 1


    # 이동하려고 하는 칸의 이동 횟수 출력
    print(boards[finish_x][finish_y])
