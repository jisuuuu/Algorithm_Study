#영어가 싫어요
def solution(numbers):
    change = {"zero": '0', "one": '1', "two": '2', "three": '3', "four": '4',
              "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}
    answer = ''
    n = 3

    while len(numbers) != 0:
        if numbers[:n] in change.keys():
            answer += change[numbers[:n]]
            numbers = numbers[n:]
            n = 3
        else:
            n += 1
    return int(answer)


if __name__ == '__main__':
    print(solution('onetwothreefourfivesixseveneightnine'))
    print(solution('onefourzerosixseven'))