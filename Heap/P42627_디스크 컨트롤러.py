# P42627. 디스크 컨트롤러
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/42627


import heapq


def solution(jobs):
    # 대기 중인 작업들
    queue = []

    # 종료된 작업들
    finished = []

    # 마지막으로 작업이 종료된 시간
    recent = -1

    # 현재 시간
    now = 0

    # 모든 요청들이 수행될 때 까지 반복문 수행
    while len(finished) != len(jobs):
        for requested_time, duration in jobs:
            # recent < requested_time: 요청된 시점이 마지막으로 작업이 종료된 시간 이후만 처리 가능
            # requested_time <= now: 현재 시간 이후로 요청된 작업만 처리 가능
            if recent < requested_time <= now:
                # (소요 시간, 요청 시간) 순으로 heapq에 삽입
                heapq.heappush(queue, (duration, requested_time))

        # 대기 중인 작업들이 있는 경우
        if queue:
            # [Key Point] 대기 중인 작업들 중에서 소요 시간이 가장 작은 것을 우선으로 처리
            duration, requested_time = heapq.heappop(queue)

            # (요청 시간, 현재 시간 + 소요 시간) = (요청 시간, 종료 시간)으로 finished에 삽입
            finished.append((requested_time, now + duration))

            # 마지막으로 작업이 종료된 시간을 변경
            recent = now

            # 현재 시간에 소요 시간을 추가
            now = now + duration

        # 대기 중인 작업들이 없는 경우
        else:
            now = now + 1


    # 평균 작업 시간 계산
    total = 0

    for requested_time, finished_time in finished:
        total = total + finished_time - requested_time

    return total // len(finished)


print(solution([[0, 3], [1, 9], [2, 6]]))   # 9
