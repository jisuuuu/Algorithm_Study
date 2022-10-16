#동전 게임
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    count = {
        'TTT': 0,
        'TTH': 0,
        'THT': 0,
        'THH': 0,
        'HTT': 0,
        'HTH': 0,
        'HHT': 0,
        'HHH': 0
    }

    word = sys.stdin.readline().rstrip()

    for i in range(38):
        count[word[i:i + 3]] += 1

    for c in count.values():
        print(c, end=' ')
    print()
