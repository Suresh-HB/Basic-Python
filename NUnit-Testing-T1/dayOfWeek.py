'''
@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-10
@Title : Take the random formated date as a user input and display the day name
'''

class Util:
    @staticmethod
    def dayOfWeek(m, d, y):
        """
        Description: Function to find the day name based on input type of date
        Parameter:
           m,d,y : Ensure inputs are integers 
        Return:
            d0, dic[d0]: returns dictionary data 'key value pair' through dictionary index
        """
        
        m = int(m)
        d = int(d)
        y = int(y)
        
    
        y0 = y - (14 - m) // 12
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = m + 12 * ((14 - m) // 12) - 2
        d0 = (d + x + (31 * m0) // 12) % 7
        
        # dictionary for day names
        dic = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
        return d0, dic[d0]


import sys


def main():
       # here i am  taking input from command line arguments
    if len(sys.argv) != 4:
        print("Usage: python script.py m d y")
        sys.exit(1)
    
    m = int(sys.argv[1])
    d = int(sys.argv[2])
    y = int(sys.argv[3])
    
    day_of_week_index, day_name = Util.dayOfWeek(m, d, y)
    print(f"Day of the week index: {day_of_week_index}")
    print(f"Day name: {day_name}")

if __name__ == "_main_":
   main()