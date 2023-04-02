# B11404. 플로이드
# [백준] https://www.acmicpc.net/problem/11404


import sys
input = sys.stdin.readline


# 무한을 의미하는 값
INF = int(1e9)


# 노드의 개수와 간선의 개수
n = int(input())
m = int(input())

# 2차원 리스트로 그래프를 만들고 모든 값을 무한으로 초기화
graph = [[INF] * n for _ in range(0, n)]

# 시작과 도착이 같으면 0으로 초기화
for a in range(0, n):
    for b in range(0, n):
        if a == b:
            graph[a][b] = 0
            
            
# 간선 정보 입력         
for _ in range(0, m):
    # a번 노드에서 b번 노드로 가는 비용은 c
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1] = min(c, graph[a - 1][b - 1])
    

# 플로이드 워셜 알고리즘 수행
# [Key Point] i -> j의 거리와, i -> k -> j의 거리를 비교
for k in range(0, n):
    for i in range(0, n):
        for j in range(0, n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            

for a in range(0, n):
    for b in range(0, n):
        # 도달할 수 없는 경우
        if graph[a][b] == INF:
            print("INF", end=" ")
        
        # 도달할 수 있는 경우
        else:
            print(graph[a][b], end=" ")
    
    print()
    