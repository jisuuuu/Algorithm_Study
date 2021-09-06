#단어 뒤집기 2
import sys
S = list(sys.stdin.readline().rstrip())
i, start = 0, 0

while i < len(S):
    if S[i] == '<':
        i += 1
        while S[i] != '>':
            i += 1
        i += 1
    elif S[i].isalnum():
        start = i

        while i < len(S) and S[i].isalnum():
            i += 1
        tmp = S[start : i]
        S[start:i] = reversed(tmp)
    else:
        i += 1


print(''.join(S))