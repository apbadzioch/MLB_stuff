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

# Asking the user for the name of the pitcher
pitcher = input("Enter the name of the pitcher you would like to analyze: ")
