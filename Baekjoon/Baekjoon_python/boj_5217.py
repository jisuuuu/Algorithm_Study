#쌍의 합
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    new = []

    print(f'Pairs for {n}: ', end='')
    for i in range(1, n // 2 + 1):
        if i != n - i:
            new.append(i)

    for i, w in enumerate(new):
        print(w, n - w, end='')

        if i != len(new) - 1:
            print(', ', end='')
    print()