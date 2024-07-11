'''
@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-10
@Title : Program Aim
     
'''

def toBinary(decimal_number):
    if decimal_number == 0:
        return '00000000'

    binary_representation = []
    max_power = 31 
    while 2 ** max_power > decimal_number:
        max_power -= 1

    for power in range(max_power, -1, -1):
        if decimal_number >= 2 ** power:
            binary_representation.append('1')
            decimal_number -= 2 ** power
        else:
            binary_representation.append('0')

    binary_string = ''.join(binary_representation)
    binary_string = binary_string.zfill(32)

    return binary_string

def main():
    decimal_number = 106
    binary_representation = toBinary(decimal_number)
    print(f"The binary representation of {decimal_number} is: {binary_representation}")


if __name__ == '__main__':
    main()