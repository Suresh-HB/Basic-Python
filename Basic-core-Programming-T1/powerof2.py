'''
@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-10 
@Title : To printing the 2^power table  
'''


import sys
class PowersOfTwo:
    def print_powers_of_two(self, N):
        if not (0 <= N < 31):
            print("Please enter a valid integer N such that 0 <= N < 31")
            return
        
        power = 1
        print(f"Powers of 2 less than or equal to 2^{N}:")
        for i in range(N + 1):
            print(f"2^{i} = {power}")
            power *= 2


def main():
    pow_of_two = PowersOfTwo()
   
    if len(sys.argv) != 2:
        print("Enter valid integer number")
    else:
        try:
            N = int(sys.argv[1])
            pow_of_two.print_powers_of_two(N)
        except ValueError:
            print("Please enter a valid integer for N")
if __name__ == "__main__":
    main()
    
