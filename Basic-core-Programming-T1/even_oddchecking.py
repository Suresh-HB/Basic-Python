'''
@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-10 
@Title : 
'''



def checkEven(num):
  """
    Description: Function to check if the number is even or odd
    Parameter:
        num : it takes input parameter for this function,it accepts dynamic integer value from user
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