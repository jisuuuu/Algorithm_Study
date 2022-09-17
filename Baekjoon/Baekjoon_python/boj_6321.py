#IBM 빼기 1
import sys
n = int(sys.stdin.readline().rstrip())

for i in range(1, n + 1):
    word = sys.stdin.readline().rstrip()
    result = ''
    print(f'String #{i}')
    for w in word:
        if ord(w) == 90:
            result += 'A'
        else:
            result += chr(ord(w) + 1)
    print(result)
    print()