#숫자 맞추기 게임
import sys

idx = 1
while True:
    n_0 = int(sys.stdin.readline().rstrip())
    if n_0 == 0:
        break
    n_1 = n_0 * 3

    if n_1 % 2 == 0:
        n_2 = n_1 // 2
        print(f'{idx}. even ', end='')
    else:
        n_2 = (n_1 + 1) // 2
        print(f'{idx}. odd ', end='')
    n_4 = (n_2 * 3) // 9
    print(n_4)
    idx += 1