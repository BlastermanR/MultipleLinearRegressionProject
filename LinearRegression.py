import pandas as pd # Sata processing, CSV file I/O (e.g. pd.read_csv)
import os # Used for obtaining path
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error, mean_absolute_error 
from sklearn import preprocessing 

####################################################################
# Links:
# Data Sets: 
# https://www.kaggle.com/datasets/nelgiriyewithana/apple-quality?resource=download ## QUALITY CHANGED TO 1 = Good, 0 = Bad
# https://www.kaggle.com/datasets/quantbruce/real-estate-price-prediction?resource=download
# https://archive.ics.uci.edu/dataset/186/wine+quality
# 
# Tutorial Used: https://www.geeksforgeeks.org/multiple-linear-regression-with-scikit-learn/
# SKLearn Install: https://scikit-learn.org/stable/install.html
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
            # Drop the first column containing the Entry IDs if present
            if (df.columns[0].find("A_id") != -1 or df.columns[0].find("No") != -1):
                df.drop(df.columns[0], axis=1, inplace=True)
            # Store the DataFrame in the dictionary with the file name as the key
            data[file_name] = df
    return data

# Prints table
def printData(metrics):
    i = 1
    for file_name in metrics:
        print("Dataset #" + str(i) + ":")
        i += 1
        print(metrics[file_name])
    return

def main():
    inputPath = os.getcwd() + "/inputs" # Specifies /input folder from executable directory
    
    # Throw error if folder does not exist
    if not os.path.exists(inputPath):
        raise FileNotFoundError(f"The folder '{inputPath}' does not exist.")
    
    files = printInputFiles(inputPath)
    metrics = readInputFiles(inputPath)
    #printData(metrics)

    for file_name in metrics:
        print("////////////////////////////////////////////////\nTesting: " + file_name)
        # Create feature variables
        # Dependant Variable
        y = metrics[file_name].iloc[:, -1]
        # Independant Variables
        X = metrics[file_name].iloc[:,:-1]
    
        # Creating train and test sets 
        XTrain, XTest, yTrain, yTest = train_test_split( X, y, test_size=0.3, random_state=101) 

        # Create model
        model = LinearRegression()
        model.fit(XTrain,yTrain)

        # Make predictions 
        predictions = model.predict(XTest) 

        # Model results 
        print( 'Mean Squared Error : ', mean_squared_error(yTest, predictions)) 
        print( 'Mean Absolute Error : ', mean_absolute_error(yTest, predictions)) 

if __name__ == "__main__":
    main()