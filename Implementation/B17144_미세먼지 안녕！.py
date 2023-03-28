# B17144. 미세먼지 안녕!
# [백준] https://www.acmicpc.net/problem/17144

import sys
input = sys.stdin.readline


# 집의 세로 크기, 집의 가로 크기, 미세먼지 확산 시간
r, c, t = map(int, input().split())

# 미세먼지의 양
house = [list(map(int, input().split())) for _ in range(0, r)]


# 미세먼지 확산
def diffusion(x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # 확산된 방향의 개수
    spread = 0

    for i in range(0, 4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 0 <= nx < r and 0 <= ny < c: 칸이 있으면 확산이 일어남
        # house[nx][ny]: 공기청정기가 없으면 확산이 일어남
        if 0 <= nx < r and 0 <= ny < c and house[nx][ny] != -1:
            spread = spread + 1
            
            # 확산되는 칸은 미세먼지 증가
            increased[nx][ny] = increased[nx][ny] + house[x][y] // 5
    
    # 현재 칸은 미세먼지 감소
    decreased[x][y] = decreased[x][y] + house[x][y] // 5 * spread


# 공기청정기 상단의 바람 순환
def purifyTop():
    # 왼쪽
    for i in range(top - 1, 0, -1):
        house[i][0] = house[i - 1][0]
        
    # 위쪽
    for i in range(0, c - 1, 1):
        house[0][i] = house[0][i + 1]

    # 오른쪽
    for i in range(0, top, 1):
        house[i][c - 1] = house[i + 1][c - 1]
        
    # 아래쪽
    for i in range(c - 1, 1, -1):
        house[top][i] = house[top][i - 1]

    house[top][1] = 0


# 공기청정기 하단의 바람 순환
def purifyBottom():
    # 왼쪽
    for i in range(bottom + 1, r - 1, 1):
        house[i][0] = house[i + 1][0]
        
    # 아래쪽
    for i in range(0, c - 1, 1):
        house[r - 1][i] = house[r - 1][i + 1]
        
    # 오른쪽
    for i in range(r - 1, bottom, -1):
        house[i][c - 1] = house[i - 1][c - 1]
        
    # 위쪽
    for i in range(c - 1, 0, -1):
        house[bottom][i] = house[bottom][i - 1]
        
    house[bottom][1] = 0


# t초 동안 미세먼지 확산
for _ in range(0, t):
    # 미세먼지가 있는 곳의 위치
    dusts = []

    # 공기청정기의 위치
    top, down = 0, 0

    for i in range(0, r):
        for j in range(0, c):
            if house[i][j] > 0:
                dusts.append((i, j))
            if house[i][j] == -1 and top == 0 and down == 0:
                top = i
                bottom = i + 1
                

    # 확산이 진행된 후 증가하는 미세먼지의 양
    increased = [[0] * c for _ in range(0, r)]
    
    # 확산이 진행된 후 감소하는 미세먼지의 양
    decreased = [[0] * c for _ in range(0, r)]

    # 미세먼지가 있는 곳에서 확산 진행
    for x, y in dusts:
        diffusion(x, y)

    # 확산이 진행된 후 증가한 미세먼지와 감소한 미세먼지의 양을 계산
    for i in range(0, r):
        for j in range(0, c):
            house[i][j] = house[i][j] + increased[i][j] - decreased[i][j]


    # 공기청정기 상단의 바람 순환 진행
    purifyTop()
    
    # 공기청정기 하단의 바람 순환 진행
    purifyBottom()


# t초 후 남아있는 미세먼지 양 계산
answer = 0

for d in house:
    answer = answer + sum([i for i in d if i != -1])


print(answer)
