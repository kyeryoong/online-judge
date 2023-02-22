# P17686. 파일명 정렬
# [프로그래머스] https://school.programmers.co.kr/learn/courses/30/lessons/17686


def solution(files):
    new_files = []
    
    for file in files:
        head = ""
        number = ""

        # 각 파일명의 한 글자씩 비교
        for j in range(0, len(file)):
            
            # 글자가 문자고 NUMBER가 없으면, HEAD에 글자를 추가
            if not(file[j].isdigit()) and not(number):
                head = head + file[j].lower()

            # 글자가 숫자고 HEAD가 있으면, NUMBER에 글자를 추가
            elif file[j].isdigit() and head:
                number = number + file[j]

            # 글자가 문자고 HEAD와 NUMBER가 있으면, 반복문 종료
            if not(file[j].isdigit()) and head and number:
                break

        # new_files에 [파일명, HEAD, NUMBER]형식으로 추가
        new_files.append([file, head, int(number)])


    # new_files를 HEAD와 NUMBER 기준으로 정렬
    new_files.sort(key=lambda x:(x[1], x[2]))


    return [new_file[0] for new_file in new_files]


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
# ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
