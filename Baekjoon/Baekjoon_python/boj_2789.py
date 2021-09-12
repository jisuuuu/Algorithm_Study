#유학 금지
import sys
word = sys.stdin.readline().rstrip()

for w in word:
    if w not in 'CAMBRIDGE':
        print(w, end='')