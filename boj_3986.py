#좋은 단어
import sys
n = int(sys.stdin.readline().rstrip())
cnt = 0
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    q = []
    for w in word:
        if not q or q[-1] != w:
            q.append(w)
        else:
            q.pop()
    if not q:
        cnt += 1
print(cnt)