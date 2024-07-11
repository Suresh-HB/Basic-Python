'''
@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-10
@Title : TemparatureConversion fahrenheit to Celsius
     
'''


class Util:
    @staticmethod
    def temperature_conversion(temp, scale):
        if scale.lower() == 'c':
            converted_temp = (temp * 9/5) + 32
            return converted_temp
        elif scale.lower() == 'f':
            converted_temp = (temp - 32) * 5/9
            return converted_temp
        else:
            raise ValueError("Invalid scale. Please use 'C' for Celsius or 'F' for Fahrenheit.")


def main():
    try:
        temp = float(input("Enter the temperature: "))
        scale = input("Enter 'C' for Celsius or 'F' for Fahrenheit: ")
        
        converted_temp = Util.temperature_conversion(temp, scale)
        
        if scale.lower() == 'c':
            print(f"{temp}°C is equal to {converted_temp}°F")
        elif scale.lower() == 'f':
            print(f"{temp}°F is equal to {converted_temp}°C")
    
    except ValueError as e:
        print(e)
        

if __name__ == "__main__":
   main()
