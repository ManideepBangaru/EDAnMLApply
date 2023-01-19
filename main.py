'''Importing libraries'''
import pandas as pd

# Importing Data
hp_df = pd.read_csv("./Datasets/house-prices-advanced-regression-techniques/train.csv")

# printing snippet of data
print(hp_df.head())
