'''
@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-10 
@Title : Checking whether user entered input is vowel or consonent 
'''


VOWEL="AEIOU"
def vowel(char):
  if char in VOWEL:
    print(f'{char} is vowel')
  else:
    print(f'{char} is consonent')


def main():
    char=input("Enter one character like *[ A B C d e f ......]\n")
    char=char.upper()
    vowel(char)


if __name__ == "__main__":
    main()