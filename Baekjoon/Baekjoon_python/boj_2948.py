#2009년
import sys
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]

d, m = map(int, sys.stdin.readline().rstrip().split())
print(days[(sum(months[:m - 1]) + d) % 7])