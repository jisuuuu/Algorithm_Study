#Count Me In
import sys
n = int(sys.stdin.readline().rstrip())
vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

for _ in range(n):
    s = sys.stdin.readline().rstrip().replace(' ', '')

    cnt = 0
    for x in s:
        if x in vowels:
            cnt += 1
    print(len(s) - cnt, cnt)
