#대표값
import sys
dictionary = dict()
nums = list()

for _ in range(10):
    n = int(sys.stdin.readline().rstrip())
    nums.append(n)

    if n not in dictionary:
        dictionary[n] = 1
    else:
        dictionary[n] += 1
print(sum(nums) // 10)
print(sorted(dictionary.items(), key=(lambda x:x[1]), reverse=True)[0][0])