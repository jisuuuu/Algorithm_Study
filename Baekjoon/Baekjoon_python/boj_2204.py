#도비의 난독증 테스트
import sys

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break

    words = [sys.stdin.readline().rstrip() for _ in range(n)]
    words.sort(key=lambda w : w.lower())

    print(words[0])