import numpy
import pandas as pd
import argparse

def analyze_csv(file_path):
    """
    loads in a csv file and comes out with basic information about the data
    """

    try:
        df = pd.read_csv(file_path)
        print()
    except FileNotFoundError:
        print("FILE NOT FOUND")
        return
    except Exception as e:
        print(e.getMessage())


    for column_name in df.columns:
        column_data = pd.to_numeric(df[column_name], errors= "coerce").dropna()

        if column_data.empty:
            print("no data")
            return
        
        np_data = column_data.to_numpy()

        mean = np.mean(np_data)
        median = np.median(np_data)
        std = np.std(np_data)
        
        print(mean)
        print(median)
        print(std)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "analyze the columns of a csv")
    
    # Add an argument for the file path
    parser.add_argument("file_path", type=str, help="The full path to the CSV file to analyze.")
    
    # Parse the arguments provided by the user
    args = parser.parse_args()
    
    # Call the main function with the user's file path
    analyze_csv(args.file_path)