# B13913. 숨바꼭질 4
# [백준] https://www.acmicpc.net/problem/13913


from collections import deque
import sys
input = sys.stdin.readline

# 수빈이와 동생의 위치
n, k = map(int, input().split())

# 현재 위치
queue = deque([n])

# 해당 위치 방문 여부
visited = [False] * 100001

# 해당 위치 방문하기 이전 위치
before_visited = [-1] * 100001


# 너비 우선 탐색 알고리즘
while queue:
    current_position = queue.popleft()

    # 동생의 위치에 도착하면 반복문 종료
    if current_position == k:
        break
    
    # current_position + 1: 뒤로 걷기
    # current_position - 1: 앞으로 걷기
    # current_position * 2: 순간이동
    for new_position in [current_position - 1, current_position + 1, current_position * 2]:
        # 이동할 위치가 범위 내에 있고, 방문한 적이 없어야 함
        if 0 <= new_position <= 100000 and not visited[new_position]:
            # 현재 위치 방문 처리
            visited[new_position] = True
            
            # 이전 위치 기록
            before_visited[new_position] = current_position
            
            queue.append(new_position)


answer = []

index = k

# 동생의 위치 -> 수빈이의 위치로 이동 (= 반대로 이동)
while True:
    answer.append(index)
    
    # 현재 위치가 수빈이의 위치면 반복문 종료
    if index == n:
        break
    
    # 이전 위치로 이동
    index = before_visited[index]
    

print(len(answer) - 1)
print(" ".join(map(str, list(reversed(answer)))))
