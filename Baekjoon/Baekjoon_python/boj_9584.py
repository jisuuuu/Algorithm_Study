#Fraud Busters
import sys
basic = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    compare = sys.stdin.readline().rstrip()

    for i in range(len(basic)):
        if basic[i] != '*':
            if compare[i] != basic[i]:
                break
    else:
        arr.append(compare)

print(len(arr))
print('\n'.join(arr))