#비밀번호 발음하기
import sys
while True:
    password = sys.stdin.readline().rstrip()

    if password == 'end':
        break

    vowels = 'aeiou'
    vowel_cnt = 0
    vowel_repeat, consonant_repeat = 0, 0
    temp = ''
    flag = True

    for p in password:
        if p in vowels:
            consonant_repeat = 0
            vowel_repeat += 1
            vowel_cnt += 1

            if vowel_repeat >= 3:
                flag = False
            if temp == p:
                if p == 'e' or p == 'o':
                    pass
                else:
                    flag = False
        else:
            vowel_repeat = 0
            consonant_repeat += 1

            if consonant_repeat >= 3:
                flag = False
            if temp == p:
                flag = False

        temp = p

    if vowel_cnt < 1:
        flag = False

    if flag:
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')