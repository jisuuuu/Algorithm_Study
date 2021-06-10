#팰린드롬인지 확인하기
import sys
s = sys.stdin.readline().rstrip()
check = 0
for i in range(len(s) // 2):
    if s[i] != s[len(s) - 1 - i]:
        break
else:
    check = 1
print(check)