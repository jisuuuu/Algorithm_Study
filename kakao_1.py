#문자열 압축
def solution(s):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1):
        prev = s[:i] #문자열 맨 처음부터 N단위로 분할한 첫 값
        new = ""
        cnt = 1
        #맨 앞부터 비교할 것이 나오는 것이 아닌 N으로 분할했으면 같은 문자열이 연속으로 나왔을 때 체크
        for j in range(i, len(s) + i, i): # N 단위로 분할했을 때 끝까지 체크하기 위해
            if prev == s[j:j + i]:
                cnt += 1

            else:
                if cnt != 1:
                    new += str(cnt)
                    new += prev
                else:
                    new += prev

                prev = s[j:j + i]
                cnt = 1
        answer = min(answer, len(new))

    return answer