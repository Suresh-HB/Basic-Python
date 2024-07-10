'''
@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-10 
@Title : Program Aim
'''


class PerfectNumberChecker:
    """
    Description: Function to check  whether entered number is perfect or not
    Parameter:
        x : Number to be checked whether is perfect or not 
    Return:
        Returns True if perfect else returns False
    """
    def __init__(self):
        pass


    def is_perfect_number(self, num):
        if num <= 0:
            return False
        

        divisors_sum = 0
        for i in range(1, num):
            if num % i == 0:
                divisors_sum += i
        return divisors_sum == num
    

def main():
    checker = PerfectNumberChecker()
    number =int(input("enter the number\n"))
    if checker.is_perfect_number(number):
        print(f"{number} is a perfect number.")
    else:
        print(f"{number} is not a perfect number.")


if __name__ == "__main__":
    main()

