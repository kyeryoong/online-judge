# B11403. 경로 찾기
# [백준] https://www.acmicpc.net/problem/11403


import sys
input = sys.stdin.readline


# 무한을 의미하는 값
INF = int(1e9)


# 정점의 개수
n = int(input())

# 인접 행렬
graph = [list(map(int, input().split())) for _ in range(0, n)]

# i에서 j로 가는 간선이 존재하지 않는 경우 무한으로 초기화
for i in range(0, n):
    for j in range(0, n):
        if graph[i][j] == 0:
            graph[i][j] == INF
        
        
# 플로이드 워셜 알고리즘 수행
for k in range(0, n):
    for i in range(0, n):
        for j in range(0, n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
   
         
for i in range(0, n):
    for j in range(0, n):
        # i에서 j로 가는 간선이 존재하면 1을 출력
        if graph[i][j] != INF:
            print(1, end=" ")
            
        # i에서 j로 가는 간선이 존재하지 않으면 0을 출력
        else:
            print(0, end=" ")
            
    print()