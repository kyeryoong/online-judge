# P68936. 쿼드압축 후 개수 세기
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/68936


import math

def solution(array):
    # 0과 1의 개수
    zero, one = 0, 0
    
    # 배열의 길이
    length = len(array)
    
    
    # 배열에서 0과 1의 개수 세기
    for i in range(0, length):
        for j in range(0, length):
            if array[i][j] == 0:
                zero = zero + 1
                
            elif array[i][j] == 1:
                one = one + 1
    
    
    # 영역의 크기: 2^10, 2^9, ... , 2^2, 2^1
    for i in range(int(math.log(length, 2)), 0, -1):
        size = 2 ** i
        
        # 영역의 크기만큼 배열을 모두 탐색
        for j in range(0, length, size):
            for k in range(0, length, size):
                check = []
                
                for l in range(0, size):
                    for m in range(0, size):
                        check.append(array[j + l][k + m])

                # 영역에 있는 숫자들이 모두 0인 경우
                if list(set(check)) == [0]:
                    for l in range(0, size):
                        for m in range(0, size):
                            array[j + l][k + m] = "X"
                    
                    zero = zero - len(check) + 1
                
                # 영역에 있는 숫자들이 모두 1인 경우
                elif list(set(check)) == [1]:
                    for l in range(0, size):
                        for m in range(0, size):
                            array[j + l][k + m] = "X"
                            
                    one = one - len(check) + 1
    
    
    return [zero, one]


print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))  # [4, 9]
print(solution([
    [1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,1],
    [0,0,0,0,1,1,1,1],
    [0,1,0,0,1,1,1,1],
    [0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,0,1],
    [0,0,0,0,1,0,0,1],
    [0,0,0,0,1,1,1,1]
])) # [10, 15]
