#다이얼
import sys
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
res = 0
words = sys.stdin.readline().rstrip()

for w in words:
    for d in dial:
        if w in d:
            res += dial.index(d) + 3

print(res)