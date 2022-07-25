#세탁소 사장 동혁
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    c = int(sys.stdin.readline().rstrip())
    answer = [0, 0, 0, 0]
    changes = [25, 10, 5, 1]

    for i in range(len(changes)):
        answer[i] += c // changes[i]
        c %= changes[i]
    print(*answer)