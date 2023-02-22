# P42587. 프린터
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/42587


def solution(priorities, location):
    # 문서를 (번호, 중요도) 형식으로 대기목록에 저장
    queue = [(i, priorities[i]) for i in range(0, len(priorities))]
    
    # 인쇄된 문서
    printed = []
    
    # 요청한 문서
    check = queue[location]
    
    # 대기목록에 문서가 남아있을 때 까지 진행
    while queue:
        # 대기목록에 있는 문서들의 중요도를 계산
        priority = [q[1] for q in queue]
        
        # 가장 앞에 있는 문서의 중요도가 가장 높으면 출력
        if queue[0][1] == max(priority):
            x = queue.pop(0)
            printed.append(x)
        
        # 가장 앞에 있는 문서의 중요도가 가장 높지 않으면, 대기목록의 가장 마지막에 넣음
        else:
            x = queue.pop(0)
            queue.append(x)
            

    # 요청한 문서가 몇 번째로 인쇄되는지 확인
    return printed.index(check) + 1


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
