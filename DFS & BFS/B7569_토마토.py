# B7569. 토마토
# [백준] https://www.acmicpc.net/problem/7569


from collections import deque
import sys
input = sys.stdin.readline


# 토마토 상자의 가로와 세로의 길이와 높이
m, n, h = map(int, input().split())

# 토마토가 있는 지점의 정보
graphs = [[list(map(int, input().split())) for _ in range(0, n)] for _ in range(0, h)]


# 토마토가 있는 지점(그래프에서 1인 지점)을 찾기
queue = deque()

for i in range(0, h):
    for j in range(0, n):
        for k in range(0, m):
            if graphs[i][j][k] == 1:
                queue.append((i, j, k))


# 너비 우선 탐색 알고리즘
def BFS():
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    while queue:
        x, y, z = queue.popleft()

        for i in range(0, 6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and graphs[nx][ny][nz] == 0:
                queue.append((nx, ny, nz))
                graphs[nx][ny][nz] = graphs[x][y][z] + 1


BFS()


answer = -1

# 그래프에서 최대값을 정답으로 출력
for i in range(0, h):
    for j in range(0, n):
        for k in range(0, m):
            if graphs[i][j][k] == 0:
                print(-1)
                exit(0)

            answer = max(answer, graphs[i][j][k])


print(answer - 1)
