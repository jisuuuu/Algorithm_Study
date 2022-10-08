#알파벳 전부 쓰기
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    word = sys.stdin.readline().rstrip().lower()

    missing_alphabet = ''

    for a in range(ord('a'), ord('z') + 1):
        if word.find(chr(a)) == -1:
            missing_alphabet += chr(a)

    if missing_alphabet == '':
        print('pangram')
    else:
        print(f'missing {missing_alphabet}')