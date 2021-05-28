#가르침 #비트 마스킹 문제 다시 풀기 작정하고
import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
word = ['a', 'n', 't', 'i', 'c']
tmp = ['' for _ in range(k - 5)]

if len(tmp) == 0:
    print(0)
    sys.exit()

cnt = 0
j = 0
for _ in range(n):
    arr = set(sys.stdin.readline().rstrip().replace('anta', '').replace('tica', ''))

    for a in arr:
        if a not in word:
            tmp[j] = a
            j += 1
            cnt += 1
