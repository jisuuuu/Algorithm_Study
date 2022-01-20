# e 계산
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return factorial(n - 1) * n


print('n e')
print('- -----------')
e = 0

for i in range(10):
    n = i
    e += factorial(i) ** (-1)

    if n < 2:
        print(f'{n} {e:.0f}')
    elif n == 2:
        print(f'{n} {e:.1f}')
    else:
        print(f'{n} {e:.9f}')