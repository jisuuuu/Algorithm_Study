#가장 먼 노드
def solution(n, edge):
    table = [[] for _ in range(n)]
    visited = [False for _ in range(n)] #방문 여부
    distances = [0 for _ in range(n)] #거리 계산

    #노드 연결
    for x, y in edge:
        table[x - 1].append(y - 1)
        table[y - 1].append(x - 1)

    #시작 노드 1인데 0으로 계산
    queue = [0]
    visited[0] = True

    while queue:
        i = queue.pop(0)

        #i에서 갈 수 있는 j 확인
        for j in table[i]:
            if visited[j] == False:
                visited[j] = True
                queue.append(j)
                distances[j] = distances[i] + 1

    return distances.count(max(distances)) #가장 먼 곳의 카운트