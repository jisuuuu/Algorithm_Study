#수 정렬하기
# 카운팅 정렬이용하기
import sys

n = int(sys.stdin.readline().rstrip())

check_list = [0] * 10001 #10000이라는 수가 들어올 수 있기 때문에
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())

    check_list[num - 1] = check_list[num - 1] + 1

for i in range(10001):
    if check_list[i] != 0:
        for j in range(check_list[i]):
            print(i + 1)