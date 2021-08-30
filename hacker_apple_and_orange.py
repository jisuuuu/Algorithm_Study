#!/bin/python3


def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    new_apples = [(a + i) for i in apples]
    new_oranges = [(b + o) for o in oranges]
    apple_cnt = 0
    orange_cnt = 0

    for a in new_apples:
        if s <= a <= t:
            apple_cnt += 1

    for o in new_oranges:
        if s <= o <= t:
            orange_cnt += 1

    print(apple_cnt)
    print(orange_cnt)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
