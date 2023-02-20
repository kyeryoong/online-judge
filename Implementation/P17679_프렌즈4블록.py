# P17679. 프렌즈4블록
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/17679


def solution(m, n, board):
    # 1차원 배열로 주어진 블록을 분할하여 2차원 배열로 변환
    board = [list(b) for b in board]

    # 블록의 모양
    types = list(set([board[i][j] for j in range(0, n) for i in range(0, m)]))


    # 4개의 블록이 같은 모양인지 확인하는 함수
    def check():
        for i in range(0, m - 1):
            for j in range(0, n - 1):
                check = sorted(list(set([
                    board[i][j],
                    board[i][j + 1],
                    board[i + 1][j],
                    board[i + 1][j + 1]
                ])))
                
                # 지워지기 전/후 4개의 블록이 모두 같은 모양인지 확인
                for t in types:
                    
                    # 4개의 블록이 같은 모양이면 대문자를 소문자로 변환
                    # 소문자로 되어있으면 해당 블록은 지워져야함을 의미함
                    if check == [t] or check == [t, t.lower()]:
                        board[i][j] = t.lower()
                        board[i][j + 1] = t.lower()
                        board[i + 1][j] = t.lower()
                        board[i + 1][j + 1] = t.lower()

        # 지워져야하는 블록을 모두 0으로 변환
        # 0으로 되어있으면 해당 블록은 비워져있음을 의미함
        for i in range(0, m):
            for j in range(0, n):
                if board[i][j].islower():
                    board[i][j] = "0"


    # 위에 있는 블록을 아래로 떨어뜨려 빈 공간을 채우는 함수
    def pullDown():
        # 각 열 마다 확인
        for i in range(0, n):
            
            # 각 열에서 0이 아닌 블록들을 모음
            temp = [board[j][i] for j in range(0, m) if board[j][i] != "0"]
            
            # 각 열에서 0을 앞으로 보냄
            temp = ["0" for _ in range(0, m - len(temp))] + temp
                        
            for j in range(0, m):
                board[j][i] = temp[j]
    

                

    # 지워지는 블록의 개수
    answer = 0

    while True:
        # check와 pullDown 함수 수행
        check()
        pullDown()

        # check와 pullDown 함수 수행 후 지워진 블록 개수 확인
        count = 0
        
        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == "0":
                    count = count + 1


        # 판이 달라졌으면 계속 반복문 수행
        if answer != count:
            answer = count

        # 판이 달라지지 않았으면 반복문 중단
        else:
            break


    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])) # 14
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])) # 15