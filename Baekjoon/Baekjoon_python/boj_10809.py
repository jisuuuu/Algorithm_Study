# 알파벳 찾기
import sys

ans = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1
    , -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

words = sys.stdin.readline().rstrip()
for i, w in enumerate(words):
    if ans[ord(w) - 97] == -1:
        ans[ord(w) - 97] = i
for a in ans:
    print(a, end=" ")
