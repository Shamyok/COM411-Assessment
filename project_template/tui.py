"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""

def option_a():
    user_input = input("Please enter one of the following options:\n [A] View Reviews by Park \n [B] Number of Reviews by park and Reviewer Location \n [C] Average Score per year by park \n [D] Average Score per park by Reviewer Location.").upper()

def option_b():
    user_input = input("Please enter one of the following options:\n [A] Most reviewed parks \n [B] Park Ranking by Nationality \n [C] Most Popular Month by Park")
while True:
    user_input = input("Please enter the letter which corresponds with your desired menu choice:\n""[A] View Data \n""[B] Visualise Data \n""[X] Exit \n")
    user_input = user_input.upper()
    if user_input == "A":
        print("You have chosen option A - View Data")
        option_a()
        break
    elif user_input == "B":
        print("You have chosen option B - Visualise Data")
        option_b()
        break
    elif user_input == "X":
        print("You have chosen option X - Exit, Goodbye")
        break
    else:
        print("Please enter a valid option")
