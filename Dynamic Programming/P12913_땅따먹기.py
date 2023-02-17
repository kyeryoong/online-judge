# P12913. 땅따먹기
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/12913


def solution(lands):
    for i in range(1, len(lands)):        
        for j in range(0, 4):
            
            # 바로 위 행에서 같은 열에 있는 수를 제외하고 최대값을 선택
            
            # 11 12 13 14
            # 21 22 23 24 이면 23 = 23 + max(11, 12, 14)
            
            lands[i][j] = lands[i][j] + max(lands[i - 1][0 : j] + lands[i - 1][j + 1 :])
        
    return max(lands[-1])


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])) # 16
