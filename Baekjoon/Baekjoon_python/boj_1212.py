#8진수 2진수
import sys
# from collections import deque
# eight = sys.stdin.readline().rstrip()
# two = ''
#
# for e in eight:
#     new = deque(bin(int(e)).replace('0b', ''))
#
#     while len(new) < 3:
#         new.appendleft('0')
#
#     two += ''.join(new)
#
# if two[0] == '0':
#     print(two[1:])
# else:
#     print(two)

print(bin(int(sys.stdin.readline().rstrip(), 8))[2:])