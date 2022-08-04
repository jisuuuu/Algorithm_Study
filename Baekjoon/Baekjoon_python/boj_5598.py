#카이사르 암호
import sys
word = sys.stdin.readline().rstrip()

for w in word:
    if 65 <= ord(w) <= 67:
        print(chr(ord(w) + 23), end='')
    else:
        print(chr(ord(w) - 3), end='')
print()