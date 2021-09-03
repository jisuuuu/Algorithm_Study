#문자열
import sys
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    print(f'{s[0]}{s[-1]}')