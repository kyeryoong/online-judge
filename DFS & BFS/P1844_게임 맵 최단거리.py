# P1844. 게임 맵 최단거리
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/1844


from collections import deque


def solution(maps):
    # 맵의 행과 열의 길이
    n, m = len(maps), len(maps[0])
        

    # 너비 우선 탐색 알고리즘
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    def BFS(x, y):
        queue = deque()
        queue.append([x, y])
        
        while queue:
            x, y = queue.popleft()
        
            for i in range(0, 4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append([nx, ny])
    
    
    # 시작 위치에서 너비 우선 탐색 알고리즘 수행
    BFS(0, 0)
    
    
    # 최단거리 출력
    if maps[n - 1][m - 1] != 1:
        return maps[n - 1][m - 1]
        
    else:
        return -1
    
    
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))  # 11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))  # -1