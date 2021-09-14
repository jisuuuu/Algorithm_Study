# 올바른 괄호
def solution(s):
    stack = []

    for i in range(len(s)):
        if ')' == s[i]:
            if not stack:
                return False
            else:
                stack.pop()
        else:
            stack.append(s[i])

    return len(stack) == 0


if __name__ == '__main__':
    print(solution('()()'))