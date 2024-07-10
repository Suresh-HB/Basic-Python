'''
@Author: Suresh
@Date: 2024-07-10
@Last Modified by: Suresh
@Last Modified: 2024-07-10 
@Title : letting user to enter number, Then checking whether user entered number is prime number or not
'''


def is_prime(x):
    """
    Description: Function to find the number passed is Prime or not
    Parameter:
        x : Number to be checked whether is Prime or not 
    Return:
        Returns True if Prime else returns False
    """

    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


def main():
    n = int(input("Enter the number: "))  
    count = 0

    print("Prime numbers up to", n, ":")
    for i in range(2, n + 1):
        if is_prime(i):
            print(i)
            count += 1

    print("Total prime numbers:", count)


if __name__ == "__main__":
    main()
