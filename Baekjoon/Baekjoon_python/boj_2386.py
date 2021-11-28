#도비의 영어공부
import sys
while True:
    s = sys.stdin.readline().rstrip()
    if s == '#':
        break

    alphabet, sentence = s[0], s[1:].lower()

    print(f'{alphabet} {sentence.count(alphabet)}')