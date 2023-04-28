# P43164. 여행경로
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/43164


from collections import deque


def solution(tickets):
    # 방문 경로가 담긴 배열
    answer = []

    # (현재 공항 위치, 방문 경로, 사용한 항공권 번호) 형태로 큐에 삽입
    queue = deque([("ICN", ["ICN"], [])])

    # 너비 우선 탐색 알고리즘
    while queue:
        current, routes, used = queue.popleft()

        # 사용한 항공권의 번호와 항공권의 개수가 동일하면 모든 경로를 방문한 것
        if len(used) == len(tickets):
            answer.append(routes)

        # 현재 공항에서 모든 항공권을 확인
        for i in range(0, len(tickets)):
            origin, dest = tickets[i]

            # [Key Point] 사용 가능한 항공권
            # 1. current == origin: 현재 공항 위치(current)와 항공권의 출발점(origin)이 동일해야 함
            # 2. i not in used: 사용한 적이 없는 항공권이어야 함
            if current == origin and i not in used:
                # 현재 공항 위치 -> 항공권의 도착점(= 다음 방문할 공항 위치)
                # 방문 경로 -> 방문 경로 + 현재 공항 위치
                # 사용한 항공권 번호 -> 사용한 항공권 번호 + 현재 사용한 항공권 번호
                queue.append((dest, routes + [dest], used + [i]))


    # 알파벳 순으로 정렬
    answer.sort()

    return answer[0]


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))   # ["ICN", "JFK", "HND", "IAD"]
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))    # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
