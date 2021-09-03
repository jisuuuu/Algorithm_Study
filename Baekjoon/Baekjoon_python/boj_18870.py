#좌표 압축
import sys

n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
check = list(sorted(set(nums)))
check_dict = {check[i] : i for i in range(len(check))}

for n in nums:
    print(check_dict[n], end=' ')
    #print(check.index(n), end=' ') 시간 초과, index 함수가 배열 전체를 확인해서 그런듯