#KMP는 왜 KMP일까?
import sys
string = sys.stdin.readline().rstrip().split('-')
ans = ''
for s in string:
    ans += s[0]
print(ans)