#문자열
import sys
a, b = sys.stdin.readline().rstrip().split()
total = 50 #최대 길이 50

for i in range(len(b) - len(a) + 1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[i + j]:
            cnt += 1

    if cnt < total:
        total = cnt

print(total)