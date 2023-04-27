# B11729. 하노이 탑 이동 순서
# [백준] https://www.acmicpc.net/problem/11729


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


# 원판의 개수
n = int(input())


# 원판의 총 이동 횟수
print(2 ** n - 1)


# 매개 변수: (원판의 개수, 출발점, 도착점, 경유점)
def hanoi(n, origin, dest, stopover):
    if n == 1:
        print(origin, dest)
    
    # [Key Point] 재귀 사용
    else:
        # 1. (n - 1)개의 원판을 출발점에서 경유점로 옮김
        hanoi(n - 1, origin, stopover, dest)
        
        # 2. 나머지 1개의 원판을 출발점에서 도착점로 옮김
        hanoi(1, origin, dest, stopover)
        
        # 3. (n - 1)개의 원판을 경유점"에서 도착점"로 옮김
        hanoi(n - 1, stopover, dest, origin)

        
# 출발점: 1번 기둥, 도착점: 3번 기둥, 경유점: 2번 기둥
hanoi(n, 1, 3, 2)
