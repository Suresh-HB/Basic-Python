'''
@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-10 
@Title : 
'''


def largest(f,s,t):
    """
    Description: Function to find out the largest element among these inputs
    Parameters:
          f s t : it takes 3 integer inputs parameter for finding biggest one
      """

  
    if f>s and f>t:
        print(f'{f} is largest')
    elif f<s and s>t:
        print(f'{s} is largest')
    else:
        print(f'{t} is largest')


def main():
    f=int(input("Enter one integer number"))
    s=int(input("Enter one integer number"))
    t=int(input("Enter one integer number"))
    largest(f,s,t)

if __name__ == '__main__':
    main()