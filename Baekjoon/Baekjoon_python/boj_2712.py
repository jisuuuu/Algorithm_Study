#미국 스타일
import sys
case = {'kg': [2.2046, 'lb'], 'l': [0.2642, 'g'],
        'lb': [0.4536, 'kg'], 'g': [3.7854, 'l']}

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    a = sys.stdin.readline().rstrip().split()
    print('{:.4f}'.format(float(a[0]) * case[a[1]][0]), case[a[1]][1])