'''
@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-10
@Title : Calculates square root for a non-negative number using Newton's method
'''


def sqrt(c):
    if c < 0:
        raise ValueError("Input must be a nonnegative number.")
    
    epsilon = 1e-15  
    t = c  

    while abs(t - c / t) > epsilon * t:
        t = (c / t + t) / 2.0
    
    return t


def main():
    c = float(input("Enter a nonnegative number: "))
    square_root = sqrt(c)
    print(f"The square root of {c} is approximately {square_root}")

if __name__ == "__main__":
   main()
