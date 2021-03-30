#통계학
import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())
ans = []
for _ in range(n):
    ans.append(int(sys.stdin.readline().rstrip()))
ans.sort()
c = Counter(ans)
cnt = c.most_common()
if len(ans) > 1:
    if cnt[0][1] == cnt[1][1]:
        mod = cnt[1][0]
    else:
        mod = cnt[0][0]
else:
    mod = cnt[0][0]

print(round(sum(ans) / len(ans)))
print(ans[int(len(ans) / 2)])
print(mod)
print(max(ans) - min(ans))