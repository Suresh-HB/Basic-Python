'''
@Author: Suresh
@Date: 2024-07-10
@Last Modified by: Suresh
@Last Modified: 2024-07-10 
@Title : Allow user to decide length of coupon and generate distinct number of coupon based on user requirement
'''


import random

def generate_random_coupon(N):
    return random.randint(0, N)

def generate_distinct_coupons(N):
    distinct_coupons = set()
    total_random_numbers = 0

    while len(distinct_coupons) <= N:
        random_coupon = generate_random_coupon(N)
        total_random_numbers += 1

        if random_coupon not in distinct_coupons:
            distinct_coupons.add(random_coupon)

    return total_random_numbers

def main():
    N = int(input("Enter the number of distinct coupon numbers (N): "))
    
    if N <= 0:
        print("N must be greater than 0.")
    else:
        total_random_numbers_needed = generate_distinct_coupons(N)
        print(f"Total random numbers needed to have all distinct numbers: {total_random_numbers_needed}")

if __name__ == "__main__":
    main()
