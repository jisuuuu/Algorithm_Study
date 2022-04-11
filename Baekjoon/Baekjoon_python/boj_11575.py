#Affine Cipher
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    s = sys.stdin.readline().rstrip()
    answer = list()

    for i in range(len(s)):
        answer.append(chr(((a * (ord(s[i]) - ord('A')) + b) % 26) + ord('A')))
    print(''.join(answer))