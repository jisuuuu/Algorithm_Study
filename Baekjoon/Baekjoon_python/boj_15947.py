#아기 석환 뚜루루 뚜루
import sys
n = int(sys.stdin.readline().rstrip()) - 1
k = n // 14
songs = ["baby", "sukhwan", "tururu", "turu", "very", "cute", "tururu",
         "turu", "in", "bed", "tururu", "turu", "baby", "sukhwan"]

if n % 14 in [3, 7, 11]:
    print(f'tu+ru*{k + 1}' if k >= 4 else 'turu' + 'ru' * k)
elif n % 14 in [2, 6, 10]:
    print(f'tu+ru*{k + 2}' if k >= 3 else 'tururu' + 'ru' * k)
else:
    print(songs[n % 14])