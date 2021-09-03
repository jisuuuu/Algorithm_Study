#가장 큰 수
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True) #문자열의 대소비교 ex)11 > 101010 왼쪽부터 아스키 숫자로 큰 수를 비교하기 때문에
    return str(int(''.join(numbers)))