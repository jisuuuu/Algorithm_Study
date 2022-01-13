#찍기
import itertools
import sys
n = int(sys.stdin.readline().rstrip())
correct_answer = sys.stdin.readline().rstrip()

sanggeun: str = 'ABCABCABCABC'
changyoung: str = 'BABCBABCBABC'
hyunjin: str = 'CCAABBCCAABB'
adrian = bruno = goran = 0

for a, b, g, i in zip(itertools.cycle(sanggeun), itertools.cycle(changyoung), itertools.cycle(hyunjin), correct_answer):
    if a == i:
        adrian += 1
    if b == i:
        bruno += 1
    if g == i:
        goran += 1

m = max(adrian, bruno, goran)
print(m)
if m == adrian:
    print('Adrian')
if m == bruno:
    print('Bruno')
if m == goran:
    print('Goran')