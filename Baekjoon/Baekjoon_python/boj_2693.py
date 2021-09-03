#N번째 큰 수
import sys


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []

    for a in arr:
        if a < pivot:
            lesser_arr.append(a)
        elif a > pivot:
            greater_arr.append(a)
        else:
            equal_arr.append(a)

    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    arr = quick_sort(arr)
    print(arr[7])