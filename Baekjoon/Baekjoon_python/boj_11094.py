#꿍 가라사대
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    words = sys.stdin.readline().rstrip()

    if 'Simon says' in words:
        print(words.replace('Simon says', ''))