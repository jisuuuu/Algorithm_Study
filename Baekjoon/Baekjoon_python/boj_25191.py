#치킨댄스를 추는 곰곰이를 본 임스
import sys
chicken = int(sys.stdin.readline().rstrip())
coke, beer = map(int, sys.stdin.readline().rstrip().split())
answer = 0

print(min(chicken, coke // 2 + beer))

