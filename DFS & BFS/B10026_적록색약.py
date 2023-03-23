# B10026. 토마토
# [백준] https://www.acmicpc.net/problem/10026


from copy import deepcopy
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


n = int(input())

graphs = [list(input().replace("\n", "")) for _ in range(0, n)]

new_graphs = deepcopy(graphs)


# 깊이 우선 탐색 알고리즘
def DFS(x, y, color):
    if not (0 <= x < n and 0 <= y < n):
        return False

    if new_graphs[x][y] == color:
        new_graphs[x][y] = "X"

        DFS(x - 1, y, color)
        DFS(x + 1, y, color)
        DFS(x, y - 1, color)
        DFS(x, y + 1, color)

        return True

    return False


# 적록색약이 아닌 사람이 봤을 때 구역의 수
count_rgb = 0

# 모든 노드들을 방문해서 구역의 수 확인
for i in range(0, n):
    for j in range(0, n):
        for color in ["R", "G", "B"]:
            if DFS(i, j, color):
                count_rgb = count_rgb + 1


new_graphs = deepcopy(graphs)


# 적록색약인 사람이 봤을 때 구역의 수
count_rb = 0

# G(초록)을 모두 R(빨강)으로 변경
for i in range(0, n):
    for j in range(0, n):
        if new_graphs[i][j] == "G":
            new_graphs[i][j] = "R"


# 모든 노드들을 방문해서 구역의 수 확인
for i in range(0, n):
    for j in range(0, n):
        for color in ["R", "B"]:
            if DFS(i, j, color):
                count_rb = count_rb + 1


print(count_rgb, count_rb)
