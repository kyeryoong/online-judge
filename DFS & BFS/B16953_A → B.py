# B16953. A → B
# [백준] https://www.acmicpc.net/problem/16953


from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


a, b = map(int, input().split())


class Solution:
    # DFS 풀이법
    def solution1(a, b):
        answer = -1

        def DFS(number, count):
            nonlocal answer

            # B로 바꿨으면 연산 횟수를 출력
            if number == b:
                answer = count
                return

            if number > b:
                return

            # 2를 곱하는 경우
            DFS(number * 2, count + 1)

            # 가장 오른쪽에 1을 추가하는 경우
            DFS(int(str(number) + "1"), count + 1)

        DFS(a, 1)
        print(answer)


    # BFS 풀이법
    def solution2(a, b):
        # 연산 횟수 초기값 설정
        answer = -1
        queue = deque([(a, 1)])

        while queue:
            number, count = queue.popleft()

            # B로 바꿨으면 연산 횟수를 출력
            if number == b:
                answer = count
                break

            # 2를 곱하는 경우
            if number * 2 <= b:
                queue.append((number * 2, count + 1))

            # 가장 오른쪽에 1을 추가하는 경우
            if int(str(number) + "1") <= b:
                queue.append((int(str(number) + "1"), count + 1))

        print(answer)
        
        
    # Top-Down 풀이법
    def solution3(a, b):
        answer = 1

        # B가 A로 될때까지 반복문 수행
        while b != a:
            temp = b
            answer = answer + 1
            
            # 가장 오른쪽에 1을 제거하는 경우
            if b % 10 == 1:
                b = b // 10

            # 2로 나누는 경우
            elif b % 2 == 0:
                b = b // 2
            
            # 값이 변하지 않으면 반복문 종료
            if temp == b:
                answer = -1
                break

        print(answer)


Solution.solution1(a, b)
Solution.solution2(a, b)
Solution.solution3(a, b)
