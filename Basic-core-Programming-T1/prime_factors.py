'''
@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-10 
@Title : Finding the prime factors of number
'''

class PrimeFactorizer:
    def __init__(self):
        pass
    
    def prime_factors_brute_force(self, N):
        factors = []
        divisor = 2
        
        while divisor * divisor <= N:
            while (N % divisor) == 0:
                factors.append(divisor)
                N //= divisor
            divisor += 1 if divisor == 2 else 2    
        
        if N > 1:
            factors.append(N)
        
        return factors


def main():
    try:
        pf = PrimeFactorizer()
        N = int(input("Enter a number to find its prime factors: "))
        if N <= 0:
            raise ValueError("Input must be a positive integer")
        
        print(f"Prime factors of {N} are:", pf.prime_factors_brute_force(N))
    
    except ValueError as ve:
        print(f"Error: {ve}")


if __name__ == "__main__":
    main()