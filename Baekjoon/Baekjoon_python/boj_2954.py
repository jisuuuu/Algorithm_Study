#창영이의 일기장
import sys
diary = sys.stdin.readline().rstrip()
answer = ''
vowels = 'aeiou'

idx = 0

while True:
    if idx >= len(diary):
        break

    answer += diary[idx]

    if diary[idx] in vowels:
        idx += 2
    idx += 1
print(answer)