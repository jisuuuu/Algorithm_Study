#줄번호
import sys
n = int(sys.stdin.readline().rstrip())

for i in range(1, n + 1):
    word = sys.stdin.readline().rstrip()
    print(f'{i}. {word}')