# B1504. 특정한 최단 경로
# [백준] https://www.acmicpc.net/problem/1504


import heapq
import sys
input = sys.stdin.readline


# 무한을 의미하는 값
INF = int(1e9)


# 정점과 간선의 개수
n, m = map(int, input().split())

# 각 정점에 연결되어 있는 간선에 대한 정보
graph = [[] for _ in range(0, n + 1)]


# 간선 정보 입력
for _ in range(0, m):
    a, b, c = map(int, input().split())
    # a/b번 정점에서 b/a번 정점으로 가는 거리는 c
    graph[a].append((b, c))
    graph[b].append((a, c))

# 반드시 거쳐야 하는 임의의 두 정점
v1, v2 = map(int, input().split())


# 다익스트라 알고리즘
def dijkstra(vertex):
    distance = [INF] * (n + 1)
    distance[vertex] = 0
    
    queue = []
    heapq.heappush(queue, (0, vertex))

    while queue:
        min_dist, min_vertex = heapq.heappop(queue)

        if distance[min_vertex] < min_dist:
            continue

        for v, d in graph[min_vertex]:
            cost = min_dist + d

            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(queue, (cost, v))

    return distance


# 1번 정점에서 다른 정점으로 가는 최단 거리
distance_one = dijkstra(1)

# v1번 정점에서 다른 정점으로 가는 최단 거리
distance_v1 = dijkstra(v1)

# v2번 정점에서 다른 정점으로 가는 최단 거리
distance_v2 = dijkstra(v2)


# 1 -> v1 최단 거리
one_to_v1 = distance_one[v1]
# 1 -> v2 최단 거리
one_to_v2 = distance_one[v2]

# v1 -> v2 최단 거리
v1_to_v2 = distance_v1[v2]
# v2 -> v1 최단 거리
v2_to_v1 = distance_v2[v1]

# v1 -> n 최단 거리
v1_to_n = distance_v1[n]
# v2 -> n 최단 거리
v2_to_n = distance_v2[n]


# 경우1. 1 -> v1 -> v2 -> n 최단 거리
route_1 = one_to_v1 + v1_to_v2 + v2_to_n

# 경우2. 1 -> v2 -> v1 -> n 최단 거리
route_2 = one_to_v2 + v2_to_v1 + v1_to_n


# 두 경우 중 최단 경로의 길이 선택
answer = min(route_1, route_2)


if answer < INF:
    print(answer)

# 경로가 없는 경우    
else:
    print(-1)