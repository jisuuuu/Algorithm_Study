import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a = n // 10
    b = n % 10
    c = 0
    check = n
    cnt = 0

    while True:
        c = a + b
        a = b
        b = c % 10
        cnt += 1

        if a * 10 + b == check:
            break
    print(cnt)