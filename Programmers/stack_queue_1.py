#탑
def solution(heights):
    answer = []

    for i, h in enumerate(heights):

        if i == 0:
            answer.append(0)

        else:
            max = h
            for j in range(i, -1, -1):
                if max < heights[j]:
                    answer.append(j + 1)
                    break
            else:
                answer.append(0)

    return answer

def solution1(h):
    ans = [0] * len(h)
    for i in range(len(h)-1, 0, -1):
        for j in range(i-1, -1, -1):
            if h[i] < h[j]:
                ans[i] = j+1
                break
    return ans