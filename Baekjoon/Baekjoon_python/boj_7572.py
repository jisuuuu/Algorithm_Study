#간지(干支)
import sys
ten = [6, 7, 8, 9, 0, 1, 2, 3, 4, 5]
tweleve = 'IJKLABCDEFGH'
n = int(sys.stdin.readline().rstrip())
print(tweleve[n % 60 % 12] + str(ten[n % 60 % 10]))
