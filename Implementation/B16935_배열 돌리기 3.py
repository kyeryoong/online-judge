# B16935. 배열 돌리기 3
# [백준] https://www.acmicpc.net/problem/16935


import sys
input = sys.stdin.readline


# 배열의 크기와, 연산 횟수
n, m, r = map(int, input().split())

# 배열
arrays = [list(map(int, input().split())) for _ in range(0, n)]

# 연산
commands = list(map(int, input().split()))


for c in commands:
    # 연산이 실행된 후 배열의 크기를 다시 계산
    n = len(arrays)
    m = len(arrays[0])

    # 1번 연산: 상하 반전
    if c == 1:
        for i in range(0, n // 2):
            arrays[i], arrays[n - i - 1] = arrays[n - i - 1], arrays[i]

    # 2번 연산: 좌우 반전
    elif c == 2:
        for i in range(0, n):
            for j in range(0, m // 2):
                arrays[i][j], arrays[i][m - j -
                                        1] = arrays[i][m - j - 1], arrays[i][j]

    # 3번 연산: 오른쪽으로 90도 회전
    elif c == 3:
        new_arrays = []
        for i in list(zip(*arrays[::-1])):
            new_arrays.append(list(i))

        arrays = new_arrays

    # 4번 연산: 왼쪽으로 90도 회전
    elif c == 4:
        new_arrays = []
        for i in list(zip(*arrays))[::-1]:
            new_arrays.append(list(i))

        arrays = new_arrays

    # 5번 연산: 오른쪽으로 그룹 이동
    elif c == 5:
        new_arrays = [[0] * m for _ in range(0, n)]

        for i in range(0, n // 2):
            for j in range(0, m // 2):
                # 1번 그룹에서 2번 그룹으로 이동
                new_arrays[i][j + m // 2] = arrays[i][j]

                # 2번 그룹에서 3번 그룹으로 이동
                new_arrays[i + n // 2][j + m // 2] = arrays[i][j + m // 2]

                # 3번 그룹에서 4번 그룹으로 이동
                new_arrays[i + n // 2][j] = arrays[i + n // 2][j + m // 2]

                # 4번 그룹에서 1번 그룹으로 이동
                new_arrays[i][j] = arrays[i + n // 2][j]

        arrays = new_arrays

    # 6번 연산: 왼쪽으로 그룹 이동
    elif c == 6:
        new_arrays = [[0] * m for _ in range(0, n)]

        for i in range(0, n // 2):
            for j in range(0, m // 2):
                # 1번 그룹에서 4번 그룹으로 이동
                new_arrays[i + n // 2][j] = arrays[i][j]

                # 4번 그룹에서 3번 그룹으로 이동
                new_arrays[i + n // 2][j + m // 2] = arrays[i + n // 2][j]

                # 3번 그룹에서 2번 그룹으로 이동
                new_arrays[i][j + m // 2] = arrays[i + n // 2][j + m // 2]

                # 2번 그룹에서 1번 그룹으로 이동
                new_arrays[i][j] = arrays[i][j + m // 2]

        arrays = new_arrays


for array in arrays:
    for a in array:
        print(a, end=" ")
    print()
