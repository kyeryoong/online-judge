# B1697. 숨바꼭질
# [백준] https://www.acmicpc.net/problem/1697


from collections import deque
import sys
input = sys.stdin.readline


# 수빈이와 동생의 위치
n, k = map(int, input().split())

# 현재 위치
queue = deque([n])

# 해당 위치 방문 시간
visited = [0] * 100001


# 너비 우선 탐색 알고리즘
while queue:
    current_position = queue.popleft()

    # 동생의 위치에 도착하면 시간 출력
    if current_position == k:
        print(visited[k])
        break

    # current_position + 1: 뒤로 걷기
    # current_position - 1: 앞으로 걷기
    # current_position * 2: 순간이동
    for new_position in [current_position + 1, current_position - 1, current_position * 2]:
        # 이동할 위치가 범위 내에 있고, 방문한 적이 없어야 함
        if 0 <= new_position <= 100000 and visited[new_position] == 0:
            # 방문 시간 기록
            visited[new_position] = visited[current_position] + 1
            
            queue.append(new_position)
