#0 = not cute / 1 = cute
import sys
n = int(sys.stdin.readline().rstrip())
cute = 0
not_cute = 0
for _ in range(n):
    n = int(sys.stdin.readline().rstrip())

    if n == 1:
        cute += 1
    else:
        not_cute += 1
if cute > not_cute:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')