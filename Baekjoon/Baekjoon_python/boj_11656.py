#접미사 배열
import sys
s = sys.stdin.readline().rstrip()
arr = []

for i in range(len(s)):
    arr.append(s[i:])
print(*sorted(arr), sep='\n')