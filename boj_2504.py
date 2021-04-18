#괄호의 값
import sys


arr = sys.stdin.readline().rstrip()

stack = []

for a in arr:
    if a == ']':
        temp = 0

        while stack:
            top = stack.pop()

            if top == '[':
                if temp == 0:
                    stack.append(3)
                else:
                    stack.append(3 * temp)
                break
            elif top == '(':
                print(0)
                exit(0)
            else:
                if temp == 0:
                    temp = int(top)
                else:
                    temp = temp + int(top)
    elif a == ')':
        temp = 0

        while stack:
            top = stack.pop()

            if top == '(':
                if temp == 0:
                    stack.append(2)
                else:
                    stack.append(2 * temp)
                break
            elif top == '[':
                print(0)
                exit(0)
            else:
                if temp == 0:
                    temp = int(top)
                else:
                    temp = temp + int(top)

    else:
        stack.append(a)

result = 0
for s in stack:
    if s == '(' or s == '[':
        print(0)
        exit(0)
    else:
        result += s

print(result)