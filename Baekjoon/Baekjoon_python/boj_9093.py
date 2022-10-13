#단어 뒤집기
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    sentence = sys.stdin.readline().rstrip().split(' ')

    for s in sentence:
        print(s[::-1], end=' ')