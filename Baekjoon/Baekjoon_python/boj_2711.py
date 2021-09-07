#오타맨 고창영
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    s = sys.stdin.readline().rstrip().split()
    idx = int(s[0])
    word = s[1]
    print(word[:idx - 1], end='')
    print(word[idx:])