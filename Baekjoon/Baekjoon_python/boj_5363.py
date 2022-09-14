#요다
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    word = sys.stdin.readline().rstrip().split()
    print(' '.join(word[2:]), end=' ')
    print(' '.join(word[:2]))