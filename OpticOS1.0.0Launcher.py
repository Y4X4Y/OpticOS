import os
import math
import time

# Start of the program

print("test")
os.system("pause")

def STARTOS():
    os.system("cls")
    os.system("pause")
    print("Hello World!")
    print()
    print("Welcome to OpticOS! :)")
    os.system("pause")

STARTOS()

while True:
    os.system("cls")
    program=int(input("What u wana do : "))
    def PROGRAM_SELECTOR(program):
        os.system("cls")
        if program<0:
            os.system("cls")
            print("Bro we not in the negatives.")
            print()
            os.system("pause")
        elif program==0:
            os.system("cls")
            print("Wow u typed 0.")
            print()
            os.system("pause")
        elif program==1:
            os.system("cls")
            print("1")
            print()
            os.system("pause")
        elif program==2:
            os.system("cls")
            print("Closing. Bye bye :)")
            time.sleep(2)
            exit()
        elif program==3:
            STARTOS()
        else:
            os.system("cls")
            print("Bro we not that high yet.")
            print()
            os.system("pause")
    PROGRAM_SELECTOR(program)