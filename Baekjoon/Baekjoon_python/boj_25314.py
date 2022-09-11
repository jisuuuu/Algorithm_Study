# 코딩은 체육과목 입니다
import sys
n = int(sys.stdin.readline().rstrip())
answer = ['long'] * (n // 4)
answer.append('int')

print(' '.join(answer))