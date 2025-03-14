# working on the actual Python file to run

# Importing the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import *

import warnings
warnings.filterwarnings('ignore')

# Importing the datasets
pitch_df = pd.read_csv('pitchStats.csv')
batter_df = pd.read_csv('batterStats.csv')

# Changing the name of the dataset
pitch = pitch_df.copy()
batter = batter_df.copy()

# renaming columns


# Filtering the data to only include the pitcher of interest
def get_pitcher_data(pitcher):
    pitcher_data = pitch[pitch['last_name, first_name'] == pitcher]
    if pitcher_data.empty:
        print(f"{pitcher} is not in the dataset.")
    else:                               
        return pitcher_data

# Filtering data for plotting historical pitch data
def plot_pitch_count_history(pitcher):
    pitcher_data = get_pitcher_data(pitcher)
    if pitcher_data is not None:
        pitch_history = pitcher_data[["pitch_count_offspeed","pitch_count_fastball","pitch_count_breaking"]]
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=pitch_history)
        plt.show()

# Putting the pitcher historical data into a GUI for easier reading
def pitcher_data_GUI(pitcher):
    pitcher_data = get_pitcher_data(pitcher)
    if pitcher is not None:
        pitch_history = pitcher_data[["pitch_count_offspeed","pitch_count_fastball","pitch_count_breaking"]]
        window = tk()
        window.title(f"{pitcher} Pitch History")
        window.geometry()
        label = Label(window, text=pitch_history)
        label.pack()
        window.mainloop()


# Filtering the data to only include the hitter of interest
def get_batter_data(hitter):
    batter_data = batter[batter['last_name, first_name'] == hitter]
    if batter_data.empty:
        print(f"{hitter} is not in the dataset.")
    else:
        return batter_data

'''
# plotting the data
def plot_pitcher_data(pitcher):
    pitcher_data = get_pitcher_data(pitcher)
    if pitcher_data is not None:
        if 'pitch_type' in pitcher_data.columns:
            pitch_type_counts = pitcher_data['pitch_type'].value_counts()
            plt.figure(figsize=(12, 6))
            sns.countplot(data=pitcher_data)
            plt.title(f'{pitcher}: Pitch Type Count')
            plt.show()'
'''
    

# Main function to run the program
def main():
    print()
    print("Welcome to my MLB data analysis program.\n")
    while True:      
        choice = input("Would you  like to analyze a pitcher or hitter? (or type 'exit' to quit): ")   
        if choice == 'pitcher':
            pitcher = input("Enter the name of the pitcher: ")
            print(get_pitcher_data(pitcher))
            # plot_pitch_count_history(pitcher)
            pitcher_data_GUI(pitcher)
        elif choice == 'hitter':
            hitter = input("Enter the name of the hitter: ")
            print(get_batter_data(hitter))
        elif choice == 'exit':
            print("Have a great day.")
            return  
        else:
            print("Please enter either 'pitcher' or 'hitter'.")

    

        
if __name__ == "__main__":
    main()