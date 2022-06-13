#Laptop Sticker
import sys
wc, hc, ws, hs = map(int, sys.stdin.readline().rstrip().split())

if (wc - ws) >= 2 and (hc - hs) >= 2:
    print(1)
else:
    print(0)