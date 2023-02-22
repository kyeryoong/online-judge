# P43020. 더 맵게
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/43020


import heapq


# 모든 음식의 스코빌 지수가 K 이상인 지 확인하는 함수
def check(scoville, K):
    for s in scoville:
        if s < K:
            return False
            
    return True


def solution(scoville, K):
    # 스코빌 지수가 담긴 배열을 Heapq로 변환
    heapq.heapify(scoville)
    
    answer = 0
    
    
    # 음식이 2개 이상이고 모든 음식의 스코빌 지수가 K 이상이 될 때 까지 반복
    while not(check(scoville, K)) and len(scoville) > 1:
        
        # 가장 맵지 않은 음식과 두 번째로 맵지 않은 음식을 heapq에서 꺼냄
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        
        # 새로운 음식을 다시 heapq에 삽입
        heapq.heappush(scoville, a + b * 2)
        answer = answer + 1
    
    
    # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
    if len(scoville) == 1 and scoville[0] < K:
        return -1
    
    else:
        return answer