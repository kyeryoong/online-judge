# B14503. 로봇 청소기
# [백준] https://www.acmicpc.net/problem/14503


import sys
input = sys.stdin.readline


# 방의 크기
n, m = map(int, input().split())

# 처음에 로봇 청소기가 있는 칸의 좌표와 로봇 청소기가 바라보는 방향
x, y, direction = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(0, n)]


# 북쪽, 서쪽, 남쪽, 동쪽
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 청소하는 칸의 개수
answer = 0


while True:
    # 현재 칸이 아직 청소되지 않은 경우
    if room[x][y] == 0:
        # 현재 칸을 청소
        room[x][y] = 2
        answer = answer + 1


    # 주변 4칸을 확인
    flag = False

    for i in range(0, 4):
        try:
            if room[x + dx[i]][y + dy[i]] == 0:
                flag = True
        except:
            pass


    # 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    if flag == False:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 후진할 수 잇으면 한 칸 후진
        if 0 <= nx < n and 0 <= ny < m and room[nx][ny] != 1:
            x = nx
            y = ny

        # 후진할 수 없으면 작동 멈춤
        else:
            break


    # 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    else:
        # 반 시계 방향으로 90도 회전
        direction = (direction + 3) % 4

        nx = x + dx[direction]
        ny = y + dy[direction]

        # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
        if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0:
            x = nx
            y = ny


# 청소하는 칸의 개수 출력
print(answer)