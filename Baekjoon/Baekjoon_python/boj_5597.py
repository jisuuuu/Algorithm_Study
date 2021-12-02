#과제 안 내신 분..?
import sys
check = [i for i in range(1, 31)]

for _ in range(28):
    n = int(sys.stdin.readline().rstrip())
    check.remove(n)
print(check[0])
print(check[1])


