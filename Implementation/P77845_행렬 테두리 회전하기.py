# P77485. 행렬 테두리 회전하기
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/77485


# 행렬의 테두리를 회전하는 함수
def rotate(before):
    rows = len(before)
    columns = len(before[0])
    
    after = [[0] * len(before[0]) for _ in range(0, len(before))]
    
    # 위쪽
    for i in range(1, columns):
        after[0][i] = before[0][i - 1]
          
    # 오른쪽          
    for i in range(1, rows):
        after[i][columns - 1] = before[i - 1][columns - 1]
    
    # 아래쪽
    for i in range(0, columns - 1):
        after[rows - 1][i] = before[rows - 1][i + 1]
    
    # 왼쪽
    for i in range(0, rows - 1):
        after[i][0] = before[i + 1][0]
    
    # 테두리 안쪽에 있는 영역은 그대로 유지
    for i in range(1, rows - 1):
        for j in range(1, columns - 1):
            after[i][j] = before[i][j]
            
    return after


def solution(rows, columns, queries):
    # 행렬을 1부터 rows x columns 까지 생성
    array = [[i * columns + j + 1 for j in range(0, columns)] for i in range(0, rows)]

    answer = []

    # 각 범위마다 행렬을 회전
    for query in queries:
        # 회전하기 이전의 행렬
        before = []
        
        for i in range(query[0], query[2] + 1):
            before.append(array[i - 1][query[1] - 1 : query[3]])
        
        # 회전하기 이후의 행렬
        after = rotate(before)
        
        for i in range(query[0], query[2] + 1):
            for j in range(query[1], query[3] + 1):
                array[i - 1][j - 1] = after[i - query[0]][j - query[1]]
        
        # 회전에 의해 위치가 바뀐 숫자들
        diff = []            
    
        for i in range(0, len(before)):
            for j in range(0, len(before[i])):
                if before[i][j] != after[i][j]:
                    diff.append(before[i][j])

        # 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자
        answer.append(min(diff))
        
    
    return answer


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))  # [8, 10, 25]
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))    # [1, 1, 5, 3]
print(solution(100, 97, [[1,1,100,97]]))    # [1]
