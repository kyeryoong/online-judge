# P86971. 전력망을 둘로 나누기
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/86971


# 깊이 우선 탐색 알고리즘
def DFS(graph, start, visited):
    visited[start] = True
        
    for i in graph[start]:
        if not visited[i]:
            DFS(graph, i, visited)
    
    # 방문한 송전탑의 개수를 반환
    return visited.count(True)


def solution(n, wires):
    answer = 1e9
                   
    # 연결되어 있는 송전탑을 하나 씩 끊어서 확인
    for wire in wires:
        x, y = wire

        graph = [[] for _ in range(0, n + 1)]

        # 송전탑을 하나 끊어서 그래프를 생성
        for t in wires:
            if t != wire:
                graph[t[0]].append(t[1])
                graph[t[1]].append(t[0])

        # 두 전력망이 가지고 있는 송전탑 개수를 계산
        a = DFS(graph, x, [False] * (n + 1))
        b = DFS(graph, y, [False] * (n + 1))

        # 송전탑 개수의 차이의 최소값을 계산
        answer = min(answer, abs(a - b))
    
    
    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))    # 3
print(solution(4, [[1, 2], [2, 3], [3, 4]]))    # 0
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))    # 1
