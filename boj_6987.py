#월드컵
import sys
from itertools import combinations


def make_team(record):
    result = []
    for i in range(0, 18, 3):
        result.append({
            'win' : record[i],
            'draw' : record[i + 1],
            'lose' : record[i + 2]
        })

    return result


def dfs(k):
    global ans

    if k == 15: # 6팀이 모두 싸우는 경우의 수 15번
        cnt = 0
        for i in range(6): # 6팀이 모두 0, 0, 0 이여야하기 때문에 체크
            if [v for v in team[i].values()] == [0] * 3:
                cnt += 1

        if cnt == 6:
            ans = 1
        return

    # 해당 조합 경우일 경우 or 아닐 경우를 생각하여 dfs
    if team[game[k][0]]['win'] and team[game[k][1]]['lose']:
        team[game[k][0]]['win'] -= 1
        team[game[k][1]]['lose'] -= 1
        dfs(k + 1)
        team[game[k][0]]['win'] += 1
        team[game[k][1]]['lose'] += 1

    if team[game[k][0]]['draw'] and team[game[k][1]]['draw']:
        team[game[k][0]]['draw'] -= 1
        team[game[k][1]]['draw'] -= 1
        dfs(k + 1)
        team[game[k][0]]['draw'] += 1
        team[game[k][1]]['draw'] += 1

    if team[game[k][0]]['lose'] and team[game[k][1]]['win']:
        team[game[k][0]]['lose'] -= 1
        team[game[k][1]]['win'] -= 1
        dfs(k + 1)
        team[game[k][0]]['lose'] += 1
        team[game[k][1]]['win'] += 1


for _ in range(4):
    team = make_team(list(map(int, sys.stdin.readline().rstrip().split())))
    game = list(combinations(range(6), 2))
    ans = 0
    dfs(0)
    print(ans, end=' ')