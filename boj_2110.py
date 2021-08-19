#공유기 설치
#몰라서 참고함
import sys
n, c = map(int, sys.stdin.readline().rstrip().split())
house = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
house.sort()

start, end, result = 1, house[-1] - house[0], 0 #end 가장 높은 좌표와 낮은 좌표의 차

while start <= end:
    mid = (start + end) // 2 # start, end 의 중간 값
    old = house[0] #배열의 가장 낮은 좌표
    cnt = 1 #거리를 mid로 두었을 때 가능한 집의 개수를 세는 변수

    for i in range(1, len(house)):
        if house[i] >= old + mid:
            cnt += 1
            old = house[i]

    if cnt >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)