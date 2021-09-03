#스택
import sys

n = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(n):
    mission = sys.stdin.readline().rstrip()

    if 'push' in mission:
        m, num = mission.split(' ')
        stack.append(num)
    elif 'top' in mission:
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
    elif 'pop' in mission:
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif 'size' in mission:
        print(len(stack))
    elif 'empty' in mission:
        if len(stack) > 0:
            print(0)
        else:
            print(1)