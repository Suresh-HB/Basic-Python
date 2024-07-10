'''
@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-10 
@Title : Swapping Numbers
'''


def swap(a,b):
  temp=a
  a=b
  b=temp
  print(f'a={a},b={b}')


def main():
  a=int(input("Enter number1\n"))
  b=int(input("Enter number2\n"))
  swap(a,b)

if __name__ == '__main__':
  main()