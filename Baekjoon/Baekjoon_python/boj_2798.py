#블랙잭
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
cards = list(map(int, sys.stdin.readline().rstrip().split()))
result = 0

for i in range(0, len(cards)):
    for j in range(i + 1, len(cards)):
        for k in range(j + 1, len(cards)):
            value = cards[i] + cards[j] + cards[k]

            if value <= m:
                result = max(result, value)
print(result)