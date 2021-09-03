#모음의 개수
arr = ['a', 'e', 'i', 'o', 'u']
import sys
word = sys.stdin.readline().rstrip()
cnt = 0
for w in word:
    if w in arr:
        cnt += 1
print(cnt)