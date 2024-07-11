'''
@Author: Suresh
@Date: 2024-07-10
@Last Modified by: Suresh
@Last Modified: 2024-07-10 
@Title : letting user to enter number, then returns the nummber in a reverse way.
'''



def reverseing(n):
  """
    Description: Function to reversing the argument
    Parameter:
        n : Incoming argument
    Return:
        Returns 0, if the argument equals to 0 ,else return argument in a reverse way
    """
  if n==0:
    return
  else:
    r=n%10
    print(r,end='')
    n=n//10
    reverseing(n)
n=int(input())
reverseing(n)


def main():
    n=int(input("Enter integer number"))
    reverseing(n)
if __name__ == "__main__":
    main()