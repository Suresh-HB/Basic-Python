'''
@Author: Suresh
@Date: 2024-07-10
@Last Modified by: Suresh
@Last Modified: 2024-07-10 
@Title : Letting user to choose particular option from list of option based on that option perform operation
'''


import time
class Stopwatch:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.start_time = time.time() * 1000  # curr time  taken in milliseconds
            self.is_running = True
            print("Stopwatch started.")
        else:
            print("Stopwatch is already running.")

    def stop(self):
        if self.is_running:
            self.end_time = time.time() * 1000 
            self.is_running = False
            elapsed_time = self.end_time - self.start_time
            print("Stopwatch stopped.")
            print(f"Elapsed time: {self.format_elapsed_time(elapsed_time)}")
        else:
            print("Stopwatch is not running.")

    def reset(self):
        self.start_time = 0
        self.end_time = 0
        self.is_running = False
        print("Stopwatch reset.")

    def format_elapsed_time(self, elapsed_time):
        seconds = elapsed_time // 1000
        milliseconds = elapsed_time % 1000
        return f"{seconds} seconds {milliseconds} milliseconds"

def main():
    stopwatch = Stopwatch()
    print("Stopwatch Program")
    while True:
        print("Options:")
        print("1. Start")
        print("2. Stop")
        print("3. Reset")
        print("4. Exit")
        choice = input("Enter your choice:\n")

        match choice:
            case '1': 
                stopwatch.start()
            case '2':
                stopwatch.stop()
            case '3': 
                stopwatch.reset()
            case '4':
                print("Exiting program.")
                break
            case _: 
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
