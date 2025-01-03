"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""
import csv
# Importing the file path from another module

from project_template.process import file_path

# Function to handle option A in the menu
def option_a():
    user_input = input("Please enter one of the following options:\n [A] View Reviews by Park \n [B] Number of Reviews by park and Reviewer Location \n [C] Average Score per year by park \n [D] Average Score per park by Reviewer Location.").upper()
    if user_input == "A":
        search_csv('data/disneyland_reviews.csv')

# Function to handle option B in the menu
def option_b():
    user_input = input("Please enter one of the following options:\n [A] Most reviewed parks \n [B] Park Ranking by Nationality \n [C] Most Popular Month by Park")

# Function to search for reviews of a specific park in the CSV file
def search_csv(filepath):
    #Prompt user for the park name to search for
    search_park = input("Please enter the name of the park you with to see the reviews for.")
    try:
        # Open the CSV file in read mode
        with open(filepath, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file) # Use DictReader to access data by column name
            matches = [] # List to store matching reviews

            # Loop through each row in the CSV file
            for row in reader:
                if search_park.lower() in row['Branch'].lower():
                    matches.append(row) # Add matching row to the matches list
        # If matches were found, display the reviews
        if matches:
            print(f"\nFound {len(matches)} reviews for park: {search_park}\n")
            for match in matches:
                # Print each matching reviews details
                print(f"Review ID: {match['Review_ID']}, Rating: {match['Rating']}, Year/Month: {match['Year_Month']}, Reviewer Location: {match['Reviewer_Location']}, Branch: {match['Branch']}")
        else:
            # If no matches were found, tell the user
            print(f"\nNo Reviews for {search_park}\n")
    except FileNotFoundError:
        # If the file is not found, handle the exception and tell the user
        print("The specified file was not found. Please check the file path and try again.")

#Main menu function to handle user choices and navigate options
def menu_choice():
    while True:
        # Display menu options and prompt the user for input
        user_input = input("Please enter the letter which corresponds with your desired menu choice:\n""[A] View Data \n""[B] Visualise Data \n""[X] Exit \n")
        user_input = user_input.upper()

        # If the user selects 'A', display data
        if user_input == "A":
            print("You have chosen option A - View Data")
            option_a()
            break
        # If the user selects 'B', visualize data
        elif user_input == "B":
            print("You have chosen option B - Visualise Data")
            option_b()
            break
        # If the user selects 'X', exit the program
        elif user_input == "X":
            print("You have chosen option X - Exit, Goodbye")
            break
        # If the user enters an invalid option, prompt again
        else:
            print("Please enter a valid option")

menu_choice()

