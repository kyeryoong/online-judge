# P68645. 삼각 달팽이
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/68645


def solution(n):
    # 삼각 달팽이 배열을 초기화
    array = [[0] * (i + 1) for i in range(0, n)]
            
    x, y = 0, 0
    
    # 아래, 오른쪽, 왼쪽 위 방향의 움직임
    dx = [1, 0, -1]
    dy = [0, 1, -1]

    # 이동 방향
    direction = 0
    
    # 회전하기 전 이동해야 할 횟수
    step = n
    
    
    # 1부터 n(n+1)/2번 까지 반복하여 삼각 달팽이 배열을 채움
    for i in range(1, n * (n + 1) // 2 + 1):
        array[x][y] = i
        
        step = step - 1
        
        # 이동해야 할 횟수가 0이되면
        if step == 0:
            
            # 방향을 전환
            direction = direction + 1
            
            # 이동해야 할 횟수를 1 감소
            n = n - 1
            step = n
        
        # 다음 칸으로 이동
        x = x + dx[direction % 3]
        y = y + dy[direction % 3]
            

    result = []
            
    for a in array:
        result = result + a
        
        
    return result


print(solution(4))  # [1,2,9,3,10,8,4,5,6,7]
print(solution(5))  # [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
print(solution(6))  # [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
