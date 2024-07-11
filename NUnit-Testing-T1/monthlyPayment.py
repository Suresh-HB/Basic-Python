'''
@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-10
@Title : calculates compound intrest for monthly payment over the years 
'''


class util:
    @staticmethod
    def monthlypayment(p,y,r):

        n=12*y
        R=r/(12*100)
        payment=p*R/(1-(1+R)**(-n))
        return payment
    
    
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py m d y")
        sys.exit(1)
    p=int(sys.argv[1])
    y=int(sys.argv[2])
    r=int(sys.argv[3])
    result=util.monthlypayment(p,y,r)
    print(result)


if __name__=='__main__':
    main()
    