#복호화
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    word = sys.stdin.readline().rstrip().replace(' ', '')

    cnt_word = [0 for _ in range(26)]

    for w in word:
        cnt_word[ord(w) - 97] += 1

    if cnt_word.count(max(cnt_word)) > 1:
        print('?')
    else:
        print(chr(97 + cnt_word.index(max(cnt_word))))