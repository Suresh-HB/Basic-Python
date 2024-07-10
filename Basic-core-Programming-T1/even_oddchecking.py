'''
@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-10 
@Title : 
'''



def checkEven(num):
  """
    Description: Function to check even or odd
    Parameter:
        x : Number to be checked wether num is Even or odd
    """
  

  if num % 2==0:
    print(f"{num} is even number")
  else:
    print(f"{num} is odd number")


def main():
    num=int(input("Enter integer number"))
    checkEven(num)


if __name__ == "__main__":
    main()