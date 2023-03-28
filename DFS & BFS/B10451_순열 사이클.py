# B10451. 내리막 길
# [백준] https://www.acmicpc.net/problem/10451


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


for _ in range(0, int(input())):
    # 정수의 개수
    n = int(input())

    graph = [0] + list(map(int, input().split()))


    # 깊이 우선 탐색 알고리즘
    def DFS(node):
        # 해당 정수 방문 처리
        visited[node] = True

        # 다음 정수
        next_node = graph[node]

        # 다음 정수가 방문되지 않았으면 방문
        if not visited[next_node]:
            DFS(next_node)


    # 각 정수 방문 여부
    visited = [False] * (n + 1)

    # 순열 사이클 개수
    answer = 0

    # 모든 정수를 차례대로 확인
    for i in range(1, n + 1):
        # 방문되지 않은 정수를 방문
        if not visited[i]:
            DFS(i)
            answer = answer + 1


    # 순열 사이클 개수 출력
    print(answer)
