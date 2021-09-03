#에디터
import sys
arr = list(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
cursor = len(arr)
new = list()

for _ in range(n):
    s = sys.stdin.readline().rstrip().split(' ')

    if s[0] == 'P':
        arr.append(s[1])
    elif s[0] == 'L' and arr != []:
        new.append(arr.pop()) #자리수 변경이니까 기존꺼 빼놓고 저장
    elif s[0] == 'D' and new != []:
        arr.append(new.pop())
    elif s[0] == 'B' and arr != []:
        arr.pop()
print(''.join(arr + list(reversed(new))))

#시간 초과
# insert, del 전부 확인하기 때문에 시간 초과
# for _ in range(n):
#     s = sys.stdin.readline().rstrip()
#
#     if 'P' in s:
#         num = s.split(' ')[1]
#         arr.insert(cursor, num)
#         cursor += 1
#     elif s == 'L':
#         if cursor != 0:
#             cursor -= 1
#     elif s == 'D':
#         if cursor != len(arr):
#             cursor += 1
#     elif s == 'B':
#         if cursor != 0:
#             del arr[cursor - 1]
#             cursor -= 1
#
# print(''.join(arr))