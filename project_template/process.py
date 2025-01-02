"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perfrom necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""

import csv
import time
def read_csv(file_path):
    data = []
    print("Reading the dataset")
    time.sleep(2)
    with open (file_path, "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    print("Finished reading the dataset")
    time.sleep(2)
    print(f"The dataset contains {len(data)} rows")
    return data

file_path = "data/disneyland_reviews.csv"
dataset = read_csv(file_path)