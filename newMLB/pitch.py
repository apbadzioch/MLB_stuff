# working on the actual Python file to run

# Importing the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#import tkinter as tk
#from tkinter import ttk

import warnings
warnings.filterwarnings('ignore')

# Importing the datasets
pitch_df = pd.read_csv('pitchStats.csv')
batter_df = pd.read_csv('batterStats.csv')

# Changing the name of the dataset
pitch = pitch_df.copy()
batter = batter_df.copy()

# Helper to reverse the name format for easier reading
def reverse_name(name):
    if ',' in name:
        last_name, first_name = name.split(', ')
        return f"{first_name} {last_name}"
    else:
        return name

# Filtering the data to only include the pitcher of interest
def get_pitcher_data(pitcher):
    pitcher_data = pitch[pitch['last_name, first_name'] == pitcher]
    if pitcher_data.empty:
        print(f"{reverse_name(pitcher)} is not in the dataset.")
    else:                               
        return pitcher_data
    
# Determine the dominant pitch type for each pitcher
def dominant_pitch(pitcher):
    # Get the data for the pitcher
    pitcher_data = get_pitcher_data(pitcher)
    if pitcher_data is not None:
        # Get the pitch type counts
        pitch_counts = pitcher_data[['pitch_count_offspeed', 'pitch_count_fastball', 'pitch_count_breaking']].sum()
        # Rename the columns for better readability when printing
        pitch_counts = pitch_counts.rename(index={
            'pitch_count_offspeed': 'offspeed',
            'pitch_count_fastball': 'fastball',
            'pitch_count_breaking': 'breaking'
        })
        # Determine the dominant pitch type
        dominant_pitch_type = pitch_counts.idxmax()
        return dominant_pitch_type
    else:
        print(f"No data available for {reverse_name(pitcher)}.")

# Getting annual data for each pitcher
def get_annual_data(pitcher):
    pitcher_data = get_pitcher_data(pitcher)
    if pitcher_data is not None:
        # Get the annual data for the pitcher
        annual_data = pitcher_data.groupby('year')[['pitch_count_offspeed', 'pitch_count_fastball', 'pitch_count_breaking']].sum()
        # Rename the columns for better readability when printing
        annual_data = annual_data.rename(columns={
            'pitch_count_offspeed': 'offspeed',
            'pitch_count_fastball': 'fastball',
            'pitch_count_breaking': 'breaking'
        })
        annual_pitch = annual_data.idxmax()
        return annual_pitch

            
    
# Plotting the dominant pitch type for each pitcher
# def plot_dominant_pitch(pitcher):

# Filtering data for plotting historical pitch data
def plot_pitch_count_history(pitcher):
    pitcher_data = get_pitcher_data(pitcher)
    if pitcher_data is not None:
        pitch_history = pitcher_data.groupby('year')[["pitch_count_offspeed","pitch_count_fastball","pitch_count_breaking"]].sum()
        plt.figure(figsize=(15, 5))
        sns.lineplot(data=pitch_history, x='year', y='pitch_count_offspeed', label='offspeed', marker='o', color='blue')
        sns.lineplot(data=pitch_history, x='year', y='pitch_count_fastball', label='fastball', marker='o', color='red')
        sns.lineplot(data=pitch_history, x='year', y='pitch_count_breaking', label='breaking', marker='o', color='green')
        
        plt.title(f"{reverse_name(pitcher)} Pitch History")
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
        window.title(f"{reverse_name(pitcher)} Pitch History")
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
        print(f"{reverse_name(hitter)} is not in the dataset.")
    else:
        return batter_data




# Main function to run the program
def main():
    print()
    print("Welcome to my MLB data analysis program.\n")

# Begin the loop to ask for input
    while True:      
        choice = input("Would you like to analyze a pitcher or hitter? (or type 'exit' to quit): ")   
        # Pitcher information
        if choice.lower() == 'pitcher':
            pitcher = input("Enter the name of the pitcher (Last, First): ")
            print(get_pitcher_data(pitcher))

        # Show the dominant pitch type
            print()
            print(f"The dominant pitch type for {reverse_name(pitcher)} is {dominant_pitch(pitcher)}.\n")

        # Show the pitch count history plot
            choice_1 = input(f"Would you like to see {pitcher}'s pitch count history plot? (yes/no): ")
            if choice_1.lower() == 'yes':
                plot_pitch_count_history(pitcher)
            else:
                print("OK, moving on.\n")

        # Show the annual data
            choice_2 = input("Would you like to see the annual breakdown of pitch types? (yes/no): ")
        
        # Hitter information
        elif choice.lower() == 'hitter':
            hitter = input("Enter the name of the hitter: ")
            print(get_batter_data(hitter))
        
        # Exiting the program
        elif choice.lower() == 'exit':
            print()
            print("Have a great day.\n")
            return  
        else:
            print("Please enter either 'pitcher' or 'hitter'.\n")


if __name__ == "__main__":
    main()
    