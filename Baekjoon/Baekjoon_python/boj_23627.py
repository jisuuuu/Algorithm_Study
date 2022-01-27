#driip
import sys
word = sys.stdin.readline().rstrip()
driip = 'driip'

for i in range(4, -1, -1):
    if word[i + len(word) - len(driip)] != driip[i]:
        print('not cute')
        break
else:
    print('cute')