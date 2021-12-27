#나이 계산하기
import sys
birthday = list(map(int, sys.stdin.readline().rstrip().split()))
standard = list(map(int, sys.stdin.readline().rstrip().split()))

#만 나이
if birthday[0] < standard[0]:
    if birthday[1] > standard[1]:
        print(standard[0] - birthday[0] - 1)
    elif birthday[1] < standard[1]:
        print(standard[0] - birthday[0])
    else:
        if birthday[2] > standard[2]:
            print(standard[0] - birthday[0] - 1)
        elif birthday[2] <= standard[2]:
            print(standard[0] - birthday[0])
else:
    print(standard[0] - birthday[0])
#세는 나이
print(standard[0] - birthday[0] + 1)
#연 나이
print(standard[0] - birthday[0])

