#평균 중앙값 문제
import sys

while True:
    a, b = map(int, sys.stdin.readline().rstrip().split())

    if a == b == 0:
        break

    print(a - (b - a))
    # c는 a보다 작으면서 b와 a의 차이값을 구해서 a보다 그 차이 값만큼 작으면 가장 작은 정수
    # a, b, c의 평균값도 a가 되고, 중앙값도 a가 됨