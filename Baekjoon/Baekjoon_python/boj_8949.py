#대충 더해
import sys
a, b = sys.stdin.readline().rstrip().split()
a_length, b_length = len(a), len(b)

if a_length > b_length:
    b = '0' * (a_length - b_length) + b
else:
    a = '0' * (b_length - a_length) + a

result = ''

for i in range(len(a)):
    result += str(int(a[i]) + int(b[i]))
print(result)