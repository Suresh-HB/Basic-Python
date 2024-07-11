'''
@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-10
@Title : Read an integer as a input, convert to Binary 
        .swapping nibbles is a four-bit aggregation and find the new number
        .Find the resultant number is the number is a power of 2
'''


def toBinary(decimal_number):
    if decimal_number == 0:
        return '00000000'

    binary_representation = format(decimal_number, '08b')
    return binary_representation


def swapNibbles(decimal_number):
    binary_string = toBinary(decimal_number)
    binary_string = binary_string.zfill(8)
    swapped_binary = binary_string[4:] + binary_string[:4]
    swapped_decimal = int(swapped_binary, 2)
    return swapped_decimal


def isPowerOfTwo(number):
    return (number != 0) and ((number & (number - 1)) == 0)


def main():
    decimal_number = int(input("Enter a decimal number: "))
    binary_representation = toBinary(decimal_number)
    print(f"Binary representation of {decimal_number} is: {binary_representation}")
    swapped_number = swapNibbles(decimal_number)
    print(f"After swapping nibbles, the resultant number is: {swapped_number}")
    if isPowerOfTwo(swapped_number):
        print("The resultant number is a power of 2.")
    else:
        print("The resultant number is not a power of 2.")

   
if __name__ == "__main__":
    main()
     

