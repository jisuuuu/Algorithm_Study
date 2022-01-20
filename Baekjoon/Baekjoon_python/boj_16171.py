#나는 친구가 적다(small)
import sys
word = sys.stdin.readline().rstrip()
check = sys.stdin.readline().rstrip()
new = []

for w in word:
    if 65 <= ord(w) < 91:
        new.append(w)
    elif 97 <= ord(w) < 123:
        new.append(w)
new = ''.join(new)

if check in new:
    print(1)
else:
    print(0)