'''
@Author: Suresh
@Date: 2024-07-10 
@Last Modified by: Suresh
@Last Modified: 2024-07-10
@Title : Program Aim
     
'''


def minimum_notes(change):

    notes = [1000, 500, 100, 50, 10, 5, 2, 1]
    result_notes = []


    def calculate_notes(amount, index):# 2 0 6 2
        
        if amount == 0:
            return 0
        if index >= len(notes):
            return float('inf')

        count_with_current_note = float('inf')
        if amount >= notes[index]:
            count_with_current_note = 1 + calculate_notes(amount - notes[index], index)

        count_without_current_note = calculate_notes(amount, index + 1)

        if count_with_current_note < count_without_current_note:
            result_notes.append(notes[index])
            return count_with_current_note
        else:
            return count_without_current_note

    min_num_notes = calculate_notes(change, 0)
    return min_num_notes, result_notes


def main():

    change = int(input("Enter the change amount in Rs: "))
    min_notes, notes_list = minimum_notes(change)
    print(f"Minimum number of notes needed: {min_notes}")
    print(f"Notes to be returned: {notes_list}")


if __name__ == "__main__":
    main()