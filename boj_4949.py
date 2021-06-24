#균형잡힌 세상
import sys
while True:
    line = sys.stdin.readline().rstrip()
    stack = []
    flag = True

    for l in line:
        if l == '(' or l == '[':
            stack.append(l)
        elif l == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
                break
        elif l == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = False
                break

    if line == '.':
        break

    if flag and not stack:
        print('yes')
    else:
        print('no')