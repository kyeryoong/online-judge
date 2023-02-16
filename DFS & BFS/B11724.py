# B11724. 연결 요소의 개수
# [백준] https://www.acmicpc.net/problem/11724


import sys
input = sys.stdin.readline


# 재귀 최대 깊이 설정
sys.setrecursionlimit(10000)


n, m = map(int, input().split())

# 테스트 케이스 입력
inputs = [list(map(int, input().split())) for _ in range(0, m)]


# 테스트 케이스를 그래프로 변환
graph = [[] for _ in range(0, n + 1)]
visited = [False] * (n + 1)

for i in inputs:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])


# 깊이 우선 탐색 알고리즘
def DFS(start):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            DFS(i)


# 연결 요소의 개수
count = 0

# 1번 노드부터 방문 시작
for i in range(1, n + 1):

    # 방문되지 않은 노드는 방문 시작
    if not visited[i]:
        DFS(i)
        count = count + 1


print(count)
