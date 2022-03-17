#수 정렬하기4
import sys
n = int(sys.stdin.readline().rstrip())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline().rstrip()))
print('\n'.join(list(map(str, sorted(nums))))) #수 정렬하기 5 reverse=True 빼기