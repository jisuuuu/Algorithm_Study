#팬그램
import sys
n = int(sys.stdin.readline().rstrip())
alphabet = list(range(97, 123))

for i in range(1, n + 1):
    pangram = sys.stdin.readline().rstrip().lower()
    check = [0 for _ in range(26)]

    for p in pangram:
        if ord(p) in alphabet:
            check[ord(p) - 97] += 1

    if min(check) == 0:
        print(f'Case {i}: Not a pangram')
    elif min(check) == 1:
        print(f'Case {i}: Pangram!')
    elif min(check) == 2:
        print(f'Case {i}: Double pangram!!')
    elif min(check) == 3:
        print(f'Case {i}: Triple pangram!!!')