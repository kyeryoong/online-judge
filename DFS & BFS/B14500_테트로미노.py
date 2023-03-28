# B14500. 테트로미노
# [백준] https://www.acmicpc.net/problem/14501


import sys
input = sys.stdin.readline


n, m = map(int, input().split())

boards = [list(map(int, input().split())) for _ in range(0, n)]
visited = [[False] * m for _ in range(0, n)]

max_value = -1

for i in range(0, n):
    max_value = max(max_value, max(boards[i]))

answer = 0


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def DFS(x, y, step, total):
    global answer

    if total + (4 - step) * max_value <= answer:
        return


    if step == 4:
        answer = max(answer, total)
        return

    for i in range(0, 4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not(visited[nx][ny]):
            if step == 2:
                visited[nx][ny] = True
                DFS(x, y, step + 1, total + boards[nx][ny])
                visited[nx][ny] = False
            
            visited[nx][ny] = True
            DFS(nx, ny, step + 1, total + boards[nx][ny])
            visited[nx][ny] = False


def T(x, y):
    global answer
    
    total = boards[i][j]
    
    


for i in range(0, n):
    for j in range(0, m):
        visited[i][j] = True
        DFS(i, j, 1, boards[i][j])
        visited[i][j] = False


print(answer)
