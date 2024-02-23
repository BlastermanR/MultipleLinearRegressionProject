import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import sklearn
    
####################################################################
# Links:
# Data Set: https://www.kaggle.com/datasets/nelgiriyewithana/apple-quality?resource=download
# 
#
####################################################################

# Prints the contents of the /inputs sub directory
def printInputFiles(): 
    input_csv_path = os.getcwd() + "/inputs" # Specifies /input folder from executable directory
    # Throw error if folder does not exist
    if not os.path.exists(input_csv_path):
        raise FileNotFoundError(f"The folder '{input_csv_path}' does not exist.")
    # Print the CSV Files to be read
    print ("Reading Files:")
    for name in os.listdir(input_csv_path):
        if name.lower().endswith('.csv'):
            print(name)

# Reads csv files in the input directory
# Return array containing Data
def readFiles(input_path):
    data = {} # Store Data

    # Loop through each file in the folder
    for file_name in os.listdir(input_path):
        file_path = os.path.join(input_path, file_name)
        # Check if the file is a CSV file
        if file_name.endswith('.csv'):
            # Read the CSV file into a Pandas DataFrame
            df = pd.read_csv(file_path)
            # Store the DataFrame in the dictionary with the file name as the key
            data[file_name] = df
    return data

def main():
    printInputFiles() # Execute this inside the CWD.

if __name__ == "__main__":
    main()