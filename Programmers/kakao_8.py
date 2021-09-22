# 2021 KAKAO BLIND RECRUITMENT 신규 아이디 추천
import re

def solution(new_id):
    #1단계
    answer = new_id.lower()
    #2단계
    answer = re.sub('[~!@#$%^&*\(\)=+\[\{\]\}:?,\<\>/]', '', answer)

    #3단계
    answer = re.sub('\.+', '.', answer)

    #4단계
    if answer:
        if answer[0] == '.':
            answer = answer[1:]

    if answer:
        if answer[-1] == '.':
            answer = answer[:-1]

    #5단계
    if not answer:
        answer = 'a'

    #6단계
    answer = answer[:15]
    if answer:
        if answer[-1] == '.':
            answer = answer[:-1]

    #7단계
    if len(answer) < 3:
        answer = answer + answer[-1]*(3 - len(answer))

    return answer

def solution(new_id):
    answer = ''
    # 1단계 & 2단계 : 소문자로 치환 및 특수문자 제거
    answer = re.sub('[^a-z\d\-\_\.]', '', new_id.lower())

    # 3단계 : 마침표 2번 이상 >  하나로
    answer = re.sub('\.\.+', '.', answer)

    # 4단계 : 양 끝 마침표 제거
    answer = re.sub('^\.|\.$', '', answer)

    # 5단게 : 빈 문자열이면 a 대입
    if answer == '':
        answer = 'a'

    # 6단계 : 길이가 16이상이면 1~15자만 남기기 & 맨 끝 마침표 제거
    answer = re.sub('\.$', '', answer[0:15])

    # 7단계 : 길이가 3이 될 때까지 반복해서 끝에 붙이기
    while len(answer) < 3:
        answer += answer[-1:]

    return answer