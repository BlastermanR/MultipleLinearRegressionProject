import numpy as np # Linear algebra
import pandas as pd # Sata processing, CSV file I/O (e.g. pd.read_csv)
import os # Used for obtaining path
import sklearn # Used for multiple linear regression functions
    
####################################################################
# Links:
# Data Set: https://www.kaggle.com/datasets/nelgiriyewithana/apple-quality?resource=download
# Tutorial Used: https://www.geeksforgeeks.org/multiple-linear-regression-with-scikit-learn/
#
####################################################################

# Prints the contents of the /inputs sub directory
# Return Array of files to read
def printInputFiles(input_csv_path): 
    files = []
    # Print the CSV Files to be read
    print ("Reading Files:")
    for name in os.listdir(input_csv_path):
        if name.lower().endswith('.csv'):
            files.append(name)
            print(name)
    return files

# Reads csv files in the input directory
# Return dictionary containing data
def readInputFiles(input_csv_path):
    data = {} # Store Data

    # Loop through each file in the folder
    for file_name in os.listdir(input_csv_path):
        file_path = os.path.join(input_csv_path, file_name)
        # Check if the file is a CSV file
        if file_name.endswith('.csv'):
            # Read the CSV file into a Pandas DataFrame
            df = pd.read_csv(file_path)
            # Drop the first column containing the Entry IDs
            df.drop(df.columns[0], axis=1, inplace=True)
            # Store the DataFrame in the dictionary with the file name as the key
            data[file_name] = df
    return data

def main():
    inputPath = os.getcwd() + "/inputs" # Specifies /input folder from executable directory
    
    # Throw error if folder does not exist
    if not os.path.exists(inputPath):
        raise FileNotFoundError(f"The folder '{inputPath}' does not exist.")
    
    files = printInputFiles(inputPath)
    parameters = readInputFiles(inputPath)

if __name__ == "__main__":
    main()