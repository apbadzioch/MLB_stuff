# working on the actual Python file to run

# Importing the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import ttk

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
        pitch_history = pitcher_data.groupby('year')[["pitch_count_offspeed","pitch_count_fastball","pitch_count_breaking"]].sum()
        plt.figure(figsize=(15, 5))
        sns.lineplot(data=pitch_history, x='year', y='pitch_count_offspeed', label='offspeed', marker='o', color='blue')
        sns.lineplot(data=pitch_history, x='year', y='pitch_count_fastball', label='fastball', marker='o', color='red')
        sns.lineplot(data=pitch_history, x='year', y='pitch_count_breaking', label='breaking', marker='o', color='green')
        
        plt.title(f"{pitcher} Pitch History")
        plt.xlabel("year")
        plt.ylabel("pitch count")
        plt.legend()
        plt.grid(True)
        plt.show()
 

# Putting the pitcher historical data into a GUI for easier reading
def pitcher_data_GUI(pitcher):
    pitcher_data = get_pitcher_data(pitcher)
    if pitcher_data is not None:
        pitch_history = pitcher_data[["year", "pitch_count_offspeed","pitch_count_fastball","pitch_count_breaking"]]
        # Creating the GUI window
        window = tk.Tk()
        window.title(f"{pitcher} Pitch History")
        window.geometry(600, 400)
        # Creating the treeview table
        tree = ttk.Treeview(window)
        tree["columns"] = ('year', 'offspeed', 'fastball', 'breaking')
        # Defining the columns
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column('year', anchor=tk.CENTER, width=80)
        tree.column('offspeed', anchor=tk.CENTER, width=120)
        tree.column('fastball', anchor=tk.CENTER, width=120)
        tree.column('breaking', anchor=tk.CENTER, width=120)
        window.mainloop()


# Filtering the data to only include the hitter of interest
def get_batter_data(hitter):
    batter_data = batter[batter['last_name, first_name'] == hitter]
    if batter_data.empty:
        print(f"{hitter} is not in the dataset.")
    else:
        return batter_data



# Main function to run the program
def main():
    print()
    print("Welcome to my MLB data analysis program.\n")
    while True:      
        choice = input("Would you  like to analyze a pitcher or hitter? (or type 'exit' to quit): ")   
        if choice == 'pitcher':
            pitcher = input("Enter the name of the pitcher: ")
            print(get_pitcher_data(pitcher))
            plot_pitch_count_history(pitcher)
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