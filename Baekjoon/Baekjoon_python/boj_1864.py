#문어 숫자
import sys
check = {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4,
         '>': 5, '&': 6, '%': 7, '/': -1}

while True:
    total = 0
    word = sys.stdin.readline().rstrip()
    if word == '#':
        break

    for i in range(len(word) - 1, -1, -1):
        total += (check[word[i]] * (8 ** (len(word) - i - 1)))
    print(total)