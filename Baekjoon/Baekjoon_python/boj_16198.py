#에너지 모으기
import sys
n = int(sys.stdin.readline().rstrip())
energy = list(map(int, sys.stdin.readline().rstrip().split()))
check = [False for _ in range(n)]
answer = 0


def solve(cnt, total):
    global answer

    if cnt == n - 2:
        if answer < total:
            answer = total
        return
    for i in range(1, n - 1): #첫번째 구슬, 마지막 구슬 사용 X
        if not check[i]:
            left, right = i - 1, i + 1
            while check[left] and left > 0: #사용 안 한 구슬 찾기
                left -= 1
            while check[right] and right < n - 1:
                right += 1
            check[i] = True
            solve(cnt + 1, total + energy[left] * energy[right])
            check[i] = False


solve(0, 0)
print(answer)