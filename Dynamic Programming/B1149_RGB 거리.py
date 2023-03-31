# B1149. RGB 거리
# [백준] https://www.acmicpc.net/problem/1149


import sys
input = sys.stdin.readline


n = int(input())

# costs[i][0]: i번 집을 빨간색으로 칠했을 때, 모든 집을 칠하는 비용의 최솟값
# costs[i][1]: i번 집을 초록색으로 칠했을 때, 모든 집을 칠하는 비용의 최솟값
# costs[i][2]: i번 집을 파란색으로 칠했을 때, 모든 집을 칠하는 비용의 최솟값
costs = [list(map(int, input().split())) for _ in range(0, n)]


for i in range(1, n):
    # 빨간색을 칠하기 위해서는 이전에 초록색 또는 파란색을 칠해야 함
    costs[i][0] = costs[i][0] + min(costs[i - 1][1], costs[i - 1][2])

    # 초록색을 칠하기 위해서는 이전에 빨간색 또는 파란색을 칠해야 함
    costs[i][1] = costs[i][1] + min(costs[i - 1][0], costs[i - 1][2])

    # 파란색을 칠하기 위해서는 이전에 빨간색 또는 초록색을 칠해야 함
    costs[i][2] = costs[i][2] + min(costs[i - 1][0], costs[i - 1][1])


print(min(costs[n - 1]))
