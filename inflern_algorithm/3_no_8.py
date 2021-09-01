#곳감(모래시계)

def rotation(arr, direction, k):
    result = [0 for _ in range(len(arr))]

    if direction == 0:
        for i in range(len(arr)):
            if i + k >= len(a):
                result[i] = arr[(i + k) % len(arr)]
            else:
                result[i] = arr[i + k]
    else:
        for i in range(len(arr)):
            if i + k >= len(a):
                result[(i + k) % len(arr)] = arr[i]
            else:
                result[i + k] = arr[i]

    return result


import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
action = [list(map(int, input().split())) for _ in range(m)]

#강사님 방법
for a in action:
    if a[1] == 0:
        for _ in range(a[2]):
            matrix[a[0] - 1].append(matrix[a[0] - 1].pop(0))
    else:
        for _ in range(a[2]):
            matrix[a[0] - 1].insert(0, matrix[a[0] - 1].pop())


# for a in action:
#     matrix[a[0] - 1] = rotation(matrix[a[0] - 1], a[1], a[2])

s, e = 0, n
total = 0
for i in range(n):
    for j in range(s, e):
        total += matrix[i][j]

    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(total)
