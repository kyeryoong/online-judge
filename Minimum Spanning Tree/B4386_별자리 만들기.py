# B4386. 별자리 만들기
# [백준] https://www.acmicpc.net/problem/4386


from itertools import combinations
import math

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


# 별의 개수
n = int(input())

# 부모 테이블을 자기 자신으로 초기화
parent = [i for i in range(0, n + 1)]

# 별의 좌표
stars = []

# 별의 좌표를 (번호, x좌표, y좌표) 형태로 입력
for i in range(1, n + 1):
    x, y = map(float, input().split())
    stars.append((i, x, y))


# 간선 정보
edges = []

# 모든 서로 다른 두 별의 일직선 거리
for star_a, star_b in list(combinations(stars, 2)):
    # 첫 번째 별의 (번호, x좌표, y좌표)
    a_index, a_x, a_y = star_a
    
    # 두 번째 별의 (번호, x좌표, y좌표)
    b_index, b_x, b_y = star_b

    # 첫 번째와 두 번째 별의 거리
    distance = math.sqrt((b_x - a_x) ** 2 + (b_y - a_y) ** 2)

    # (두 별의 거리, 첫 번째 별의 번호, 두 번째 별의 번호) 형태로 간선 정보를 삽입
    edges.append((distance, a_index, b_index))


# 간선을 거리순으로 정렬
edges.sort()

# 최종 비용
answer = 0

# 모든 간선을 하나씩 확인
for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        answer = answer + cost


# 소수점 둘째자리까지 출력
print("%.2f" % answer)
