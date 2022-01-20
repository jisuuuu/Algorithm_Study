#팬그램
import sys
import string

while True:
    word = sys.stdin.readline().rstrip().replace(' ', '')
    alphabet = dict.fromkeys(string.ascii_lowercase, 0)
    if word == '*':
        break

    for w in word:
        alphabet[w] += 1

    # print(alphabet)
    if 0 in alphabet.values():
        print('N')
    else:
        print('Y')
