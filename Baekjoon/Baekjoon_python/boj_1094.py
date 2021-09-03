#막대기
#이진수로 바꿨을 때 1이 몇 개인지
import sys
x = int(sys.stdin.readline().rstrip())
x_list = list(bin(x).lstrip('0b'))
print(x_list.count('1'))

cnt = 0
sticks = [64, 32, 16, 8, 4, 2, 1]

for s in sticks:
    if x >= s:
        cnt += 1
        x -= s
    if x == 0:
        break
print(cnt)