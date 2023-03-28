# B1991. 트리
# [백준] https://www.acmicpc.net/problem/1991


import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


# 이진 트리의 노드 개수
n = int(input())

# 이진 트리
tree = {}


for _ in range(0, n):
    root, left, right = input().split()
    tree[root] = left, right


# 전위 순회
def preorder(root):
    if root != ".":
        print(root, end="")
        preorder(tree[root][0])
        preorder(tree[root][1])


# 중위 순회
def inorder(root):
    if root != ".":
        inorder(tree[root][0])
        print(root, end="")
        inorder(tree[root][1])


# 후위 순회
def postorder(root):
    if root != ".":
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end="")
        
        
preorder("A")   # ABDCEFG
print()
inorder("A")    # DBAECFG
print()
postorder("A")  # DBEGFCA
    