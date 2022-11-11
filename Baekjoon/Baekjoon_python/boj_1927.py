#최소 힙
import sys, heapq
n = int(sys.stdin.readline().rstrip())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())

    if x != 0:
        heapq.heappush(heap, x)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)