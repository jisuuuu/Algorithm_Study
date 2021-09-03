#부녀회장이 될테야
import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())

    room = [i for i in range(1, 16)] #0층 초기화

    for i in range(k):
        for j in range(1, n + 1):
            room[j] = room[j - 1] + room[j] #덮어쓰기로 더하는 과정
    print(room[n - 1])