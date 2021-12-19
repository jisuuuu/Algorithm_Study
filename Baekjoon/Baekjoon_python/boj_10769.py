#행복한지 슬픈지
import sys

sentance = sys.stdin.readline().rstrip()
happy = sad = 0
check = []

for s in sentance:
    if s == ':':
        check.append(s)
    elif s == '-':
        check.append(s)
    elif s == ')':
        if check == [':', '-']:
            happy += 1
            check = []
    elif s == '(':
        if check == [':', '-']:
            sad += 1
            check = []
    else:
        if check:
            check = []

if happy > sad:
    print('happy')
elif happy < sad:
    print('sad')
elif happy == sad == 0:
    print('none')
else:
    print('unsure')