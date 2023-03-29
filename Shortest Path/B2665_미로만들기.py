# B2665. 미로 만들기
# [백준] https://www.acmicpc.net/problem/2665


import heapq
import sys
input = sys.stdin.readline


# 무한을 의미하는 값
INF = int(1e9)

# 한 줄에 들어가는 방의 수
n = int(input())

graph = [list(map(int, input().rstrip())) for _ in range(0, n)]


# [Key Point] 초기 상태에는 흰 방이 1, 검은 방이 0으로 설정됨
# 반대로, 흰 방을 0으로 검은 방을 1로 변환하면, 검은 방을 지날 때 마다 비용 1을 추가하는 것으로 계산
for i in range(0, n):
    for j in range(0, n):
        if graph[i][j] == 0:
            graph[i][j] = 1

        else:
            graph[i][j] = 0


# 다익스트라 알고리즘
def dijkstra():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    distance = [[INF] * n for _ in range(0, n)]

    queue = []
    heapq.heappush(queue, (graph[0][0], (0, 0)))

    while queue:
        min_dist, min_vertex = heapq.heappop(queue)
        min_x, min_y = min_vertex

        for i in range(0, 4):
            nx = min_x + dx[i]
            ny = min_y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                cost = min_dist + graph[nx][ny]

                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(queue, (cost, (nx, ny)))

    return distance


# 다익스트라 알고리즘 수행
print(dijkstra()[n - 1][n - 1])
