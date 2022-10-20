#패라티
import sys

while True:
    bit_string = sys.stdin.readline().rstrip()
    if bit_string == '#':
        break

    check = bit_string[-1]
    bit_string = bit_string[:-1]
    bit_cnt = bit_string.count('1')

    if check == 'e':
        if bit_cnt % 2 == 0:
            bit_string += '0'
        else:
            bit_string += '1'
    else:
        if bit_cnt % 2 == 0:
            bit_string += '1'
        else:
            bit_string += '0'

    print(bit_string)