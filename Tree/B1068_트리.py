# B1068. 트리
# [백준] https://www.acmicpc.net/problem/1068


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


# 트리의 노드 개수
n = int(input())

# 트리
tree = {i : [] for i in range(0, n)}

inputs = list(map(int, input().split()))

# 제거할 노드의 번호
target = int(input())


for i in range(0, n):
    try:
        tree[inputs[i]] = tree[inputs[i]] + [i]
    except:
        pass
    
# 노드 제거
def delete(root):
    # 삭제할 노드의 모든 자손을 먼저 제거
    for i in tree[root]:
        delete(i)
    
    # 삭제할 노드 자신을 제거
    del tree[root]

# 삭제할 노드를 자손으로 가진 노드를 제거
for i in tree:
    if target in tree[i]:
        tree[i].remove(target)
        

delete(target)


# 리프 노드 개수
answer = 0

for i in tree:
    if tree[i] == []:
        answer = answer + 1
        
        
print(answer)
