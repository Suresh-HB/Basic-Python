'''
@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-10 
@Title : Leap year checking
'''


class Leap:

    
    def is_leap_year(self, year):
        """
            Description: Function to check if the year leap year or not
            Parameters:
                year : takes year as a input for this function to check leap year
        """


        if len(str(year)) != 4:
            print("Please enter a valid 4-digit year.")
            return
        
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} is a Leap Year")
        else:
            print(f"{year} is not a Leap Year")


def main():
    l = Leap()
    year = int(input("Enter a year (4 digits): "))
    l.is_leap_year(year)


if __name__ == "__main__":
    main()
     
