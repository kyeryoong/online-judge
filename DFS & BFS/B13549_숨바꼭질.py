# B13549. 숨바꼭질
# [백준] https://www.acmicpc.net/problem/13549


import heapq
import sys
input = sys.stdin.readline


# 수빈이와 동생의 위치
n, k = map(int, input().split())

# (현재 시간, 현재 위치)
queue = [(0, n)]

# 해당 위치 방문 여부
visited = [False] * 100001


# 너비 우선 탐색 알고리즘
while queue:
    # 탐색 시간이 가장 짧은 것을 우선으로 방문
    current_time, current_position = heapq.heappop(queue)

    # 동생의 위치에 도착하면 시간 출력
    if current_position == k:
        print(current_time)
        break

    # current_position * 2: 순간이동(시간 증가 없음)
    # 이동할 위치가 범위 내에 있고, 방문했던적이 없어야 함
    if 0 <= current_position * 2 <= 100000 and visited[current_position * 2] == 0:
        # 시간을 증가하지 않고 heapq에 삽입
        heapq.heappush(queue, (current_time, current_position * 2))
        visited[current_position * 2] = True

    # current_position + 1: 뒤로 걷기(1초 증가)
    # current_position - 1: 앞으로 걷기(1초 증가)
    for new_position in [current_position + 1, current_position - 1]:
        # 이동할 위치가 범위 내에 있고, 방문했던적이 없어야 함
        if 0 <= new_position <= 100000 and visited[new_position] == 0:
            # 시간을 1초 증가시키고 heapq에 삽입
            heapq.heappush(queue, (current_time + 1, new_position))
            visited[new_position] = True
