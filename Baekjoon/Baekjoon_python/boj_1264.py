#모음의 개수
import sys
while True:
    word = sys.stdin.readline().rstrip()
    if word == '#':
        break
    count = 0

    for w in word:
        if w in 'aeiouAEIOU':
            count += 1
    print(count)