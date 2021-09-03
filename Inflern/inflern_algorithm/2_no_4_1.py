#최소값 구하기
arr = [5, 3, 7, 9, 2, 5, 2, 6]
arr_min = float('inf')

for a in arr:
    if a < arr_min:
        arr_min = a
print(arr_min)