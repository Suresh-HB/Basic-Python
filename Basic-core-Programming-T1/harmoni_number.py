'''
@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-10 
@Title : 
'''


def harmonic(n):
    
    
    if n == 0:
        print("enter the positive number")
        return 
    harmonic =0.0
    for i in range(1,n+1):
        harmonic+=1/i
    print(f"the {n} hormonic number is : {harmonic}")


def main():
    n=int(input("Enter the integer number\n"))
    harmonic(n)

if __name__ =='__main__':
    main()

    