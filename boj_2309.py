#일곱난쟁이
import sys


def dfs(cnt, idx):
    if cnt == 7:
        res, ans = 0, []

        for i in range(9):
            if check[i]:
                res += boys[i]
                ans.append(boys[i])

        if res == 100:
            ans.sort()
            for a in ans:
                print(a)
            sys.exit() #dfs 함수 안에서 출력하기 때문에 무조건 sys.exit()
        return

    for i in range(idx, 9):
        check[i] = 1
        dfs(cnt + 1, i + 1)
        check[i] = 0


boys = []
for _ in range(9):
    boys.append(int(sys.stdin.readline().rstrip()))
check = [0 for _ in range(9)]
dfs(0, 0)