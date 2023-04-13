# B11725. 트리의 부모 찾기
# [백준] https://www.acmicpc.net/problem/11725


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


# 노드의 개수
n = int(input())

graphs = [[] for _ in range(0, n + 1)]


# 트리 상에서 연결된 두 노드의 정보를 입력
for _ in range(0, n - 1):
    a, b = map(int, input().split())

    graphs[a].append(b)
    graphs[b].append(a)


# 각 노드의 부모
# parents[i]: i번째의 노드의 부모, 초기에는 0으로 설정됨
parents = [0] * (n + 1)


# 깊이 탐색 우선 알고리즘
def DFS(vertex):
    # 현재 노드와 연결된 노드를 하나씩 확인
    for i in graphs[vertex]:
        # 연결된 노드의 부모가 아직 0으로 되어있으면, 현재 노드를 부모로 설정
        if parents[i] == 0:
            parents[i] = vertex
            DFS(i)


# 트리의 루트는 1이므로, 1부터 탐색 시작
DFS(1)

# 2번 노드부터 부모 노드 번호를 출력
for i in range(2, n + 1):
    print(parents[i])
