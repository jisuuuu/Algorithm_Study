# 카드1
import sys
n = int(sys.stdin.readline().rstrip())
cards = [i for i in range(1, n + 1)]
trash_cards = []

while len(cards) != 1:
    trash_cards.append(cards.pop(0))
    cards.append(cards.pop(0))

trash_cards.append(cards.pop(0))

print(*trash_cards)