#명령 프롬포트
import sys
n = int(sys.stdin.readline().rstrip())
arr = list(sys.stdin.readline().rstrip() for _ in range(n))
ans = ''
for i in range(len(arr[0])):
    a = arr[0][i]
    for j in range(1, len(arr)):
        if arr[j][i] != a:
            ans += '?'
            break
    else:
        ans += a
print(ans)