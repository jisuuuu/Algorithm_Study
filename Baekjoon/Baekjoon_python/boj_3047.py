#ABC
import sys
abc = ['A', 'B', 'C']
nums = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
dictionary = dict(zip(abc, nums))
location = sys.stdin.readline().rstrip()

for l in location:
    print(dictionary[l], end=' ')