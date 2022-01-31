#String
import sys
letters = sys.stdin.readline().rstrip()
answer = ''
temp = ''

for l in letters:
    if temp != l:
        answer += l
    temp = l
print(answer)