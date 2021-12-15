#좋은놈 나쁜놈
import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    hero = sys.stdin.readline().rstrip()
    new = hero.lower()
    if new.count('b') > new.count('g'):
        print(f'{hero} is A BADDY')
    elif new.count('b') < new.count('g'):
        print(f'{hero} is GOOD')
    else:
        print(f'{hero} is NEUTRAL')
