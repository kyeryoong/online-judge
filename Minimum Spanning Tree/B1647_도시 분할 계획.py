# B1647. 도시 분할 계획
# [백준] https://www.acmicpc.net/problem/1647


import sys
input = sys.stdin.readline


# 원소가 속한 집합을 찾기
def find(x):
    if parent[x] == x:
        return x
    
    return find(parent[x])


# 두 원소가 속한 집합을 합치기
def union(a, b):
    a = find(a)
    b = find(b)
    
    if a > b:
        parent[b] = a
        
    else:
        parent[a] = b
        

# 노드의 개수와 간선의 개수       
n, m = map(int, input().split())

# 부모 테이블을 자기 자신으로 초기화
parent = [i for i in range(0, n + 1)]


# 간선 정보
edges = []

# 간선 정보 입력
for _ in range(0, m):
    # a번 집과 b번 집을 연결하는 길의 유지비는 c
    a, b, c = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((c, a, b))


# 간선을 비용순으로 정렬
edges.sort()

# 최종 비용
answer = 0

# [Key Point] 두 마을에 있는 길의 유지비의 최소값 = (한 마을에 있는 길로 구성한 최소 신장 트리) - (최소 스패닝 트리에 있는 길 중 유지비가 가장 큰 값)
# 유지비가 가장 큰 간선
longest = -1

# 모든 간선을 하나씩 확인
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        answer = answer + cost
        longest = max(longest, cost)
        

print(answer - longest)
