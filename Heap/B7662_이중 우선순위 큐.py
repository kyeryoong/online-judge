# B7662. 이중 우선순위 큐
# [백준] https://www.acmicpc.net/problem/7662


import heapq
import sys
input = sys.stdin.readline


for _ in range(0, int(input())):
    # 연산의 개수
    k = int(input())

    # 현재 큐에 있는 지 확인
    # True: 큐에 있는 상태
    # False: 큐에 없는 상태
    heap = [False] * k

    # 최대 힙
    max_heap = []

    # 최소 힙
    min_heap = []

    for i in range(0, k):
        command, value = input().split()

        # 삽입 연산
        if command == "I":
            # [Key Point] 힙에 (값, 삽입 순서)로 삽입
            heapq.heappush(max_heap, (-int(value), i))
            heapq.heappush(min_heap, (int(value), i))

            # 큐의 상태를 True로 변경
            heap[i] = True

        # 삭제 연산
        elif max_heap and min_heap:
            # 최댓값 삭제
            if value == "1":
                # 최대 힙의 최댓값(맨 앞에 있는 값)이 현재 큐에 없는 경우
                # 최대 힙의 최댓값(맨 앞에 있는 값)이 현재 큐에 있는 상태가 될 때 까지 계속 반복
                while max_heap and not heap[max_heap[0][1]]:
                    heapq.heappop(max_heap)

                # 최댓값이 현재 큐에 있는 경우
                if max_heap:
                    # 큐의 상태를 False로 변경
                    heap[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

            # 최솟값 삭제
            else:
                # 최소 힙의 최소값(맨 앞에 있는 값)이 현재 큐에 없는 경우
                # 최소 힙의 최솟값(맨 앞에 있는 값)이 현재 큐에 있는 상태가 될 때 까지 계속 반복
                while min_heap and not heap[min_heap[0][1]]:
                    heapq.heappop(min_heap)

                # 최솟값이 현재 큐에 있는 경우
                if min_heap:
                    # 큐의 상태를 False로 변경
                    heap[min_heap[0][1]] = False
                    heapq.heappop(min_heap)


    # 최대 힙의 최댓값(맨 앞에 있는 값)이 현재 큐에 없는 경우
    # 최대 힙의 최댓값(맨 앞에 있는 값)이 현재 큐에 있는 상태가 될 때 까지 계속 반복
    while max_heap and not heap[max_heap[0][1]]:
        heapq.heappop(max_heap)

    # 최소 힙의 최소값(맨 앞에 있는 값)이 현재 큐에 없는 경우
    # 최소 힙의 최솟값(맨 앞에 있는 값)이 현재 큐에 있는 상태가 될 때 까지 계속 반복
    while min_heap and not heap[min_heap[0][1]]:
        heapq.heappop(min_heap)


    # 최대 힙과 최소 힙에 숫자가 남은 경우 = 큐에 숫자가 남은 경우
    if max_heap and min_heap:
        print(-heapq.heappop(max_heap)[0], heapq.heappop(min_heap)[0])

    # 최대 힙과 최소 힙에 숫자가 없는 경우 = 큐에 숫자가 없는 경우
    else:
        print("EMPTY")
