#단어 정렬
import sys

n = int(sys.stdin.readline().rstrip())
words = []

for _ in range(n):
    words.append(sys.stdin.readline().rstrip())

words = list(set(words))
words = sorted(words, key=lambda x:(len(x), x))

for w in words:
    print(w)