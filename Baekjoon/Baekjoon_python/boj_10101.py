#삼각형 외우기
import sys
arr = []

for _ in range(3):
    arr.append(int(sys.stdin.readline().rstrip()))

if sum(arr) != 180:
    print('Error')
elif len(set(arr)) == 1:
    print('Equilateral')
elif len(set(arr)) == 2:
    print('Isosceles')
elif len(set(arr)) == 3:
    print('Scalene')