# B1922. 네트워크 연결
# [백준] https://www.acmicpc.net/problem/1922


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


# 컴퓨터의 수와 연결할 수 있는 선의 수
n = int(input())
m = int(input())

# 부모 테이블을 자기 자신으로 초기화
parent = [i for i in range(0, n + 1)]

# 연결할 수 있는 선을 담을 리스트
edges = []

# 컴퓨터 연결 정보 입력
for _ in range(0, m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

# 연결을 비용순으로 정렬
edges.sort()

# 최종 비용
answer = 0

# 모든 연결을 하나씩 확인
for cost, a, b in edges:
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find(a) != find(b):
        union(a, b)
        answer = answer + cost


print(answer)
