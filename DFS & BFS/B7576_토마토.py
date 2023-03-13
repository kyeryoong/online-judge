# B7576. 토마토
# [백준] https://www.acmicpc.net/problem/7576


from collections import deque
import sys
input = sys.stdin.readline


# 토마토 상자의 가로와 세로 길이
m, n = map(int, input().split())

# 토마토가 있는 지점의 정보
graphs = [list(map(int, input().split())) for _ in range(0, n)]


# 토마토가 있는 지점(그래프에서 1인 지점)을 찾기
queue = deque()

for i in range(0, n):
    for j in range(0, m):
        if graphs[i][j] == 1:
            queue.append((i, j))


# 너비 우선 탐색 알고리즘
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def BFS():
    while queue:
        x, y = queue.popleft()

        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graphs[nx][ny] == 0:
                queue.append((nx, ny))
                graphs[nx][ny] = graphs[x][y] + 1


BFS()


answer = -1

# 그래프에서 최대값을 정답으로 출력
for i in range(0, n):
    for j in range(0, m):
        if graphs[i][j] == 0:
            print(-1)
            exit(0)

        answer = max(answer, graphs[i][j])


print(answer - 1)
