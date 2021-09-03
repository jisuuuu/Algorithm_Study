#숫자 야구
from itertools import permutations


def guess(base, n):
    num = list(map(int, str(base[0])))
    guess_s = base[1]
    guess_b = base[2]
    strike, ball = 0, 0

    for i in range(3):
        if num[i] == n[i]:
            strike += 1
            continue
        if num[i] in n:
            ball += 1

    if strike == guess_s and ball == guess_b:
        return True
    else:
        return False


def solution(baseball):
    answer = 0
    numbers = list(permutations([i for i in range(1, 10)], 3))

    for n in numbers:
        flag = True
        for base in baseball:
            if guess(base, n) == False:
                flag = False

        if flag == True:
            answer += 1

    return answer