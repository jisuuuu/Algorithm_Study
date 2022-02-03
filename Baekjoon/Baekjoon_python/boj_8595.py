#히든 넘버
import sys
n = int(sys.stdin.readline().rstrip())
word = sys.stdin.readline().rstrip()
total = 0
number = ''

for w in word:
    if w.isdigit() and len(number) < 6:
        number += w
    elif w.isalpha() and number:
        total += int(number)
        number = ''
if number:
    total += int(number)
print(total)