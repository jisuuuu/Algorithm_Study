#가위 바위 보?
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    player1, player2 = 0, 0

    for _ in range(n):
        p1, p2 = sys.stdin.readline().rstrip().split()

        if p1 == 'R':
            if p2 == 'P':
                player2 += 1
            elif p2 == 'S':
                player1 += 1
        elif p1 == 'P':
            if p2 == 'S':
                player2 += 1
            elif p2 == 'R':
                player1 += 1
        elif p1 == 'S':
            if p2 == 'R':
                player2 += 1
            elif p2 == 'P':
                player1 += 1

    if player1 > player2:
        print('Player 1')
    elif player1 < player2:
        print('Player 2')
    else:
        print('TIE')