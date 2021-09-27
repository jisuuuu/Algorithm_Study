#월간 코드 챌린지 시즌3 없는 숫자 더하기
def solution(numbers):
    answer = 0
    nums = [0 for _ in range(10)]

    for n in numbers:
        if nums[n] == 0:
            nums[n] = 1

    for i, n in enumerate(nums):
        if n == 0:
            answer += i
    return answer