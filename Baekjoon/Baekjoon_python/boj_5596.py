#시험 점수
import sys
minkuk = sum(list(map(int, sys.stdin.readline().rstrip().split())))
mansea = sum(list(map(int, sys.stdin.readline().rstrip().split())))

if minkuk >= mansea:
    print(minkuk)
else:
    print(mansea)