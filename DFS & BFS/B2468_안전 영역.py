# B2468. 안전 영역
# [백준] https://www.acmicpc.net/problem/2468


from copy import deepcopy
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


n = int(input())

graphs = [list(map(int, input().split())) for _ in range(0, n)]

new_graphs = deepcopy(graphs)


# 최대 비가 내린 높이 계산
max_rain_height = 0

for i in range(0, n):
    for j in range(0, n):
        max_rain_height = max(max_rain_height, graphs[i][j])


# 깊이 우선 탐색 알고리즘

def DFS(x, y, rain):
    if not(0 <= x < n and 0 <= y < n):
        return False

    if new_graphs[x][y] != "X" and new_graphs[x][y] > rain:
        new_graphs[x][y] = "X"

        DFS(x, y - 1, rain)
        DFS(x, y + 1, rain)
        DFS(x - 1, y, rain)
        DFS(x + 1, y, rain)

        return True

    return False


# 안전한 영역 개수
answer = 0


# 비가 내린 높이별로 안전한 영역 개수 계산
for rain_height in range(0, max_rain_height):
    count = 0

    new_graphs = deepcopy(graphs)

    for i in range(0, n):
        for j in range(0, n):
            if DFS(i, j, rain_height):
                count = count + 1

    answer = max(answer, count)


print(answer)
