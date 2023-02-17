# P131701. 뉴스 클러스터링
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/131701


def solution(elements):
    # 수열을 두 배로 늘려서 확인
    circular_elements = elements * 2
        
    answer = []
    
    # 크기가 1 ~ (수열의 길이)인 연속 부분 수열의 합을 계산
    for size in range(1, len(elements) + 1):
        for i in range(0, len(elements)):
            answer.append(sum(circular_elements[i : i + size]))
    
    # 중복되는 값을 제거        
    answer = list(set(answer))
    
    return len(answer)


print(solution([7,9,1,1,4]))    # 18
    