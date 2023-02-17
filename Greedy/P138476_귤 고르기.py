# P138476. 귤 고르기
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/138476


from collections import Counter

def solution(k, tangerine):
    # [Key Point] 귤의 크기로 분류했을 때, 크기별로 개수가 많은 것 순서로 담아야 함
    count = Counter(tangerine).most_common()
    count.sort(key=lambda x:x[1], reverse=True)
    
    
    answer = 0
    
    for i in range(0, len(count)):
        answer = answer + count[i][1]
        
        # 귤의 개수를 초과하면 더 이상 담지 않음
        if answer >= k:
            break
            
            
    return i + 1


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3],	3)) # 3
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3],	2)) # 2
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3],	1)) # 1
