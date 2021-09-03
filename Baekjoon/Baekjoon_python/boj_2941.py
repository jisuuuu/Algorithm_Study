#크로아티아 알파벳

import sys
word = sys.stdin.readline().rstrip()
alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for a in alpha:
    word = word.replace(a, '*')
print(len(word))