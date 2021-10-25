#팰린드롬수
import sys

while True:
    word = sys.stdin.readline().rstrip()

    if word == '0':
        break

    for i in range(len(word) // 2):
        if word[i] != word[len(word) - i - 1]:
            print('no')
            break
    else:
        print('yes')