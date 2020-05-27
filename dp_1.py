#N으로 표현N으로 표현
def solution(N, number):
    # 1. [ SET x 8 ] 초기화
    s = [ set() for x in range(8) ]

    # 2. 각 set마다 기본 수 "N" * i 수 초기화
    for i,x in enumerate(s, start=1):
        x.add( int( str(N) * i ) )

    # 3. n 일반화
    #   {
    #       "n" * i U
    #       1번 set 사칙연산 n-1번 set U
    #       2번 set 사칙연산 n-2번 set U
    #       ...
    #       n-1번 set 사칙연산 1번 set,
    #    }
    # number를 가장 최소로 만드는 수 구함.
    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)

        if  number in s[i]:
            answer = i + 1
            break

    else:
        answer = -1

    return answer


def solution(N, number):
    answer = -1
    dp = []

    for i in range(1, 9):
        numbers = set()
        numbers.add(int(str(N) * i))

        for j in range(0, i - 1):
            for x in dp[j]:
                for y in dp[-j - 1]:
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(x * y)

                    if y != 0:
                        numbers.add(x // y)

        if number in numbers:
            answer = i
            break

        dp.append(numbers)

    return answer