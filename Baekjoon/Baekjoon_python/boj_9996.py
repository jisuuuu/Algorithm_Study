#한국이 그리웅ㄹ 땐 서버에 접속하지
import sys
n = int(sys.stdin.readline().rstrip())
pattern = sys.stdin.readline().rstrip().split('*')

for _ in range(n):
    word = sys.stdin.readline().rstrip()

    if word[:len(pattern[0])] == pattern[0] and word[-len(pattern[1]):] == pattern[1] \
        and len(''.join(pattern)) <= len(word):
        print('DA')
    else:
        print('NE')