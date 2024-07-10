'''
@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-10 
@Title : PrimeFactorization for number
'''


def calculate_quotient_remainder(dividend, divisor):
  dividend=int(dividend)
  divisor=int(divisor)
  quotient = dividend // divisor
  remainder = dividend % divisor
  print(f"quotient of the number is = {quotient}")
  print(f"remainder of the number is = {remainder}")


def main():
  dividend=int(input("Enter integer dividend"))
  divisor=int(input("Enter integer divisor"))
  calculate_quotient_remainder(dividend, divisor)


if __name__ == '__main__':
  main()