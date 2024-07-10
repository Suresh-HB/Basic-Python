'''
@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-10 
@Title : 
'''


import random
class Coin:
 

 def flip_coin(num_flips):
    """
    Description: Function to counts heads and tails counts and prints percentage of each
    Parameter:
       num_flips : num_flips to be checked wether num_flips is less then or equal to zero, if it is zero retuns, if not proceed to further operation 
    """


    if num_flips <= 0:
        print("Please enter a positive integer for the number of flips.")
        return
        
    heads_count = 0
    tails_count = 0


    for _ in range(num_flips):
        coin_flip = random.random() 

        if coin_flip < 0.5:
            heads_count += 1
        else:
            tails_count += 1


    heads_percentage = (heads_count / num_flips) * 100
    tails_percentage = (tails_count / num_flips) * 100

    
    print(f"Number of flips: {num_flips}")
    print(f"Heads count: {heads_count}, Percentage: {heads_percentage:.2f}%")
    print(f"Tails count: {tails_count}, Percentage: {tails_percentage:.2f}%")


def main():
    coin=Coin()
    num_flips = int(input("Enter the number of times to flip the coin: "))
    coin.flip_coin(num_flips)


if __name__ =='__main__':
    main()
