# B1916. 최소비용 구하기
# [백준] https://www.acmicpc.net/problem/1916


import heapq
import sys
input = sys.stdin.readline


# 무한을 의미하는 값
INF = int(1e9)


# 도시와 버스의 개수
n = int(input())
m = int(input())

# 각 도시에 연결되어 있는 버스에 대한 정보
graph = [[] for _ in range(0, n + 1)]


# 버스 정보 입력
for _ in range(0, m):
    # a 도시에서 b 도시로 가는 비용은 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# 출발점과 도착점
start, end = map(int, input().split())

   
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


# 출발점에서 다익스트라 알고리즘 수행
distance = dijkstra(start)


# 도착점까지 가는데 드는 최소 비용 출력
print(distance[end])
