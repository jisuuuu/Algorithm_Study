#상근날드
import sys
hamburger = sys.maxsize
drink = sys.maxsize
for _ in range(3):
    new = int(sys.stdin.readline().rstrip())

    if hamburger > new:
        hamburger = new
for _ in range(2):
    new = int(sys.stdin.readline().rstrip())

    if drink > new:
        drink = new

print(hamburger + drink - 50)