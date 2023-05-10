# B12581. 숨바꼭질 2
# [백준] https://www.acmicpc.net/problem/12581


from collections import deque
import sys
input = sys.stdin.readline


# 수빈이와 동생의 위치
n, k = map(int, input().split())

# 현재 위치
queue = deque([n])

# 방문 시간
# -1이면 방문한 적이 없음을 의미
visited_time = [-1] * 100001

# 방문 가능한 경우의 수
visited_ways = [0] * 100001

# 수빈이의 현재 위치에서 방문 시간과 방문 가능한 경우의 수를 초기화
visited_time[n] = 0
visited_ways[n] = 1


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
        # 이동할 위치가 범위 내에 있어야 함
        if 0 <= new_position <= 100000:
            # 방문한 적이 없는 경우
            if visited_time[new_position] == -1:
                # (현재 위치 방문 시간) = (이전 위치 방문 시간) + 1
                visited_time[new_position] = visited_time[current_position] + 1 
                
                # (현재 위치 방문 가능한 경우의 수) = (이전 위치 방문 가능한 경우의 수)
                visited_ways[new_position] = visited_ways[current_position]
                
                queue.append(new_position)
                
            # 방문한 적이 있는 경우
            # 가장 빠른 시간으로 방문한 경우 -> 경우의 수 추가
            elif visited_time[new_position] == visited_time[current_position] + 1:
                visited_ways[new_position] = visited_ways[new_position] + visited_ways[current_position]
            
            
print(visited_time[k])
print(visited_ways[k])
