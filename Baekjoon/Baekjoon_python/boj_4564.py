#숫자 카드 놀이
import sys
while True:
    n = sys.stdin.readline().rstrip()
    if n == '0':
        break

    while len(n) > 1:
        answer = 1
        print(n, end=' ')

        for i in n:
            answer *= int(i)

        n = str(answer)
    print(n)