# B2458. 키 순서
# [백준] https://www.acmicpc.net/problem/2458


import sys
input = sys.stdin.readline


# 무한을 의미하는 값
INF = int(1e9)


# 학생의 수와 두 학생 키를 비교한 횟수
n, m = map(int, input().split())

# 2차원 리스트로 그래프를 만들고 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(0, n + 1)]

# 시작과 도착이 같으면 0으로 초기화
for a in range(0, n):
    for b in range(0, n):
        if a == b:
            graph[a][b] = 0

# 간선 정보 입력
for _ in range(0, m):
    # a 학생보다 b 학생이 더 큰 경우 노드를 연결
    a, b = map(int, input().split())
    graph[a][b] = 1


# 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


answer = 0


# [Key Point] (자신보다 작은 학생의 수) + (자신보다 큰 학생의 수) = (자신을 제외한 전체 학생의 수)를 만족하면 자신의 키가 몇 번째인지 알 수 있음
# graph[i][j] > 0: i 학생은 j 학생보다 작음
# graph[j][i] > 0: j 학생은 i 학생보다 작음 = i 학생은 j 학생보다 큼
for i in range(1, n + 1):
    # 자신보다 작은 학생의 수
    shorter = 0
    
    # 자신보다 큰 학생의 수
    taller = 0

    for j in range(1, n + 1):
        if 0 < graph[i][j] < INF:
            shorter = shorter + 1

        if 0 < graph[j][i] < INF:
            taller = taller + 1

    if shorter + taller == n - 1:
        answer = answer + 1


print(answer)
