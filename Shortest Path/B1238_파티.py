# B1238. 파티
# [백준] https://www.acmicpc.net/problem/1238


import heapq
import sys
input = sys.stdin.readline


# 무한을 의미하는 값
INF = int(1e9)


# 마을의 수, 도로의 개수, 파티를 벌일 장소
n, m, x = map(int, input().split())

# 각 마을에 연결되어 있는 도로에 대한 정보
graph = [[] for _ in range(0, n + 1)]


# 도로 정보 입력
for _ in range(0, m):
    # a 마을에서 b 마을로 가는 시간은 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


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


# 다른 마을에서 x 마을로 가는 시간
goto = [INF] * (n + 1)

# x 마을에서 다른 마을로 가는 시간
goback = [INF] * (n + 1)


# 모든 마을에서 다익스트라 알고리즘 수행
for i in range(1, n + 1):
    temp = dijkstra(i)

    if i == x:
        goback = temp

    else:
        goto[i] = temp[x]
        
        
# k 마을에서 x 마을을 경유하고 다시 k 마을로 가는 시간
# (k : 1 ~ n, k != x)
answer = [INF] * (n + 1)

for i in range(1, n + 1):
    answer[i] = goto[i] + goback[i]


# 가장 오래 걸리는 마을의 소요시간 출력
print(max([i for i in answer if i < INF]))
