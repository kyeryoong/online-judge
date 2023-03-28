# B1520. 내리막 길
# [백준] https://www.acmicpc.net/problem/1520


import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 7)


# 지도의 세로와 가로 크기
m, n = map(int, input().split())

# 지도 정보
maps = [list(map(int, input().split())) for _ in range(0, m)]


# [Key Point] dp[a][b]: (a, b)에서 (m, n)까지 이동 가능한 경로의 수
# 즉, (0, 0)에서 (m, n)까지 이동 가능한 경로의 수를 구하기 위해서는 dp[0][0]을 찾아야 함
dp = [[-1] * n for _ in range(0, m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def DFS(x, y):
    # 도착 지점에 도달했으면 1을 리턴(한 가지 경로)
    if x == m - 1 and y == n - 1:
        return 1

    # 해당 지점을 이미 방문했으면, 시작점에서 해당 지점까지 이동 가능한 경로의 수를 반환
    if dp[x][y] != -1:
        return dp[x][y]

    # 해당 지점을 방문한적이 없는 경우
    dp[x][y] = 0

    for i in range(0, 4):
        nx = x + dx[i]
        ny = y + dy[i]

        # (현재 지점)에서 (도착 지점)까지 이동 가능한 경로의 수 = (이동할 수 있는 지점)에서 (도착 지점)까지 이동 가능한 모든 경로의 수의 합

        # (a, b)에서 이동할 수 있는 지점이 (a + i1, b + j1), (a + i2, b + j2)이면
        # dp[a][b] = dp[a + i1][b + j1] + dp[a + i2][b + j2]
        
        # maps[nx][ny] < maps[x][y]: 이동할 수 있는 지점(nx, ny)은 현재 지점(x, y)보다 더 낮아야 함
        if 0 <= nx < m and 0 <= ny < n and maps[nx][ny] < maps[x][y]:
            dp[x][y] = dp[x][y] + DFS(nx, ny)

    return dp[x][y]


# (0, 0)에서 (m, n)까지 이동 가능한 경로의 수 계산
print(DFS(0, 0))
