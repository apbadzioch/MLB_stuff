# working on the actual Python file to run

# Importing the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Importing the datasets
pitch = pd.read_csv('pitchStats.csv')
batter = pd.read_csv('batterStats.csv')

# Filtering the data to only include the pitcher of interest
def get_pitcher_data(pitcher):
    pitcher_data = pitch[pitch['last_name, first_name'] == pitcher]
    if pitcher_data.empty:
        print(f"This pitcher is not in the dataset {pitcher}.");
    else:                               
        return pitcher_data

def get_batter_data(batterr):
    batter_data = batter[batter['last_name, first_name'] == batterr]
    if batter_data.empty:
        print(f"This batter is not in the dataset, {batterr}.");
    else:
        return batter_data


def main():
    pitcher = input("Enter the name of the pitcher you would like to analyze: ")    
    batter = input("Enter the name of the batter you would like to analyze: ")

    print(get_pitcher_data(pitcher))
    print(get_batter_data(batter))
    
    
    
    
if __name__ == "__main__":
    main()