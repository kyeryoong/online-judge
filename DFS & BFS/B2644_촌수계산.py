# B2644. 촌수계산
# [백준] https://www.acmicpc.net/problem/2644


from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


# BFS(너비 우선 탐색)을 사용
def solutionBFS(n, a, b, relations):
    # 각 사람들 간의 촌수
    distance = [0] * (n + 1)

    queue = deque([a])

    # 너비 우선 탐색 알고리즘
    while queue:
        current = queue.popleft()

        for i in relations[current]:
            # 해당 사람을 방문하지 않았으면 방문
            if distance[i] == 0:
                queue.append(i)
                distance[i] = distance[current] + 1

    # 촌수를 계산할 수 있는 경우
    if distance[b]:
        print(distance[b])

    # 촌수를 계산할 수 없는 경우
    else:
        print(-1)


# DFS(깊이 우선 탐색)을 사용
def solutionDFS(n, a, b, relations):
    # 각 사람들 간의 촌수
    distance = [0] * (n + 1)
    
    # 깊이 우선 탐색 알고리즘
    def DFS(node):           
        for i in relations[node]:
            # 해당 사람을 방문하지 않았으면 방문
            if distance[i] == 0:
                distance[i] = distance[node] + 1
                DFS(i)

    # 깊이 우선 탐색 알고리즘 실행
    DFS(a)

    # 촌수를 계산할 수 있는 경우
    if distance[b]:
        print(distance[b])

    # 촌수를 계산할 수 없는 경우
    else:
        print(-1)


# 전체 사람의 수
n = int(input())

# 촌수를 계산해야 하는 서로 다른 두 사람의 번호
a, b = map(int, input().split())

# 부모 자식들 간의 관계의 수
m = int(input())

# 부모 자식들 간의 관계
relations = [[] for _ in range(0, n + 1)]

for _ in range(0, m):
    x, y = map(int, input().split())
    relations[x].append(y)
    relations[y].append(x)


solutionBFS(n, a, b, relations)
solutionDFS(n, a, b, relations)