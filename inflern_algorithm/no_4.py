#대표값
import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
arr = list(map(int, input().split()))
avg = sum(arr) // len(arr)
