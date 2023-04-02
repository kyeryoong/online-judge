# P12927. 야근 지수
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/12927


import heapq


def solution(n, works):
    # 작업량이 담긴 배열을 최대 힙(Max Heap)으로 변환
    works = [-w for w in works]
    heapq.heapify(works)

    # 시간이 남아있을 때 까지 작업을 처리
    while n > 0 and works:
        # 작업량이 가장 많이 남은 일을 힙에서 꺼냄
        x = heapq.heappop(works)

        # 작업량이 0이 되면 힙에 넣지 않음
        if x < 0:
            # 작업량을 1만큼 처리하고 다시 힙에 넣음
            heapq.heappush(works, x + 1)

        n = n - 1

    # 남은 작업량에 대해 야근 지수를 계산
    return sum([w ** 2 for w in works])
