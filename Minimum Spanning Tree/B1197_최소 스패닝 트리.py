# B1197. 최소 스패닝 트리
# [백준] https://www.acmicpc.net/problem/1197


import sys
input = sys.stdin.readline


# 원소가 속한 집합을 찾기
def find(x):
    if parent[x] == x:
        return x

    # 루트 노드가 아니면, 루트 노드를 찾을 때 까지 재귀적으로 호출
    parent[x] = find(parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        parent[b] = a

    else:
        parent[a] = b


# 노드의 개수와 간선의 개수
v, e = map(int, input().split())

# 부모 테이블을 자기 자신으로 초기화
parent = [i for i in range(0, v + 1)]

# 간선을 담을 리스트
edges = []

# 간선 정보 입력
for _ in range(0, e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 최종 비용
answer = 0

# 모든 간선을 하나씩 확인
for cost, a, b in edges:
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find(a) != find(b):
        union(a, b)
        answer = answer + cost


print(answer)
