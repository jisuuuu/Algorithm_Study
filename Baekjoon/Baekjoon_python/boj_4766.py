#일반 화학 실험
import sys
temp = float(sys.stdin.readline().rstrip())

while True:
    num = sys.stdin.readline().rstrip()

    if num == '999':
        break

    print('{:.2f}'.format(float(num) - temp))
    temp = float(num)