#괄호
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    arr = sys.stdin.readline().rstrip()
    stack = []
    check = True
    for a in arr:
        if a == ')':
            if stack:
                stack.pop()
            else:
                check = False
        else:
            stack.append(a)

    if check is False or stack:
        print('NO')
    else:
        print('YES')