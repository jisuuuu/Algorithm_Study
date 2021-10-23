#방 번호
import sys
n = sys.stdin.readline().rstrip()
check = [0 for _ in range(10)]

for i in range(len(n)):
    num = int(n[i])

    if num == 6 or num == 9:
        if check[6] <= check[9]:
            check[6] += 1
        else:
            check[9] += 1
    else:
        check[num] += 1
print(max(check))
