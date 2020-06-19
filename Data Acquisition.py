""" Below, I have imported a csv file that was downloaded from kaggle. This file is a dataset that includes information
gathered from anonymous persons about their annual income. The income levels are divided into two brackets, salaries
less than or equal to $50,000, and salaries more than $50,000. The dataset also includes a variety of demographic info
such as: age, occupation, race, native nationality, education level, etc..

The purpose of my project is to present the salaries of these anonymous people and explore possible trends/relationships
between different variables such as race, gender, education, etc."""

import pandas as pd
import csv
import statistics

import pypyodbc as pypyodbc


df = pd.read_csv (r'https://github.com/Dsmity/MIS-5400-Final-Project.git/adult-income.csv')

df.rename(columns={'39': 'Age'}, inplace=True)
df.rename(columns={'State-gov': 'Sector'}, inplace=True)
df.rename(columns={'Bachelors': 'Education level'}, inplace=True)
df.rename(columns={'Never-married': 'Marital status'}, inplace=True)
df.rename(columns={'Adm-clerical': 'Employment field'}, inplace=True)
df.rename(columns={'White': 'Race'}, inplace=True)
df.rename(columns={'Male': 'Gender'}, inplace=True)
df = df.drop(df.columns[[2, 4, 7, 10, 11]], axis=1)
df = df.drop(df)

print(df)

""" With the code above, I am attempting to format and cleanse some of the data before loading it in a separate datbase, 
hopefully that will make it easier to query the information I'm looking for. I am trying to rename some of the 
columns to have more descriptive and meaningful labels, as-well-as remove a few of the columns that aren't as 
necessary for the purpose of this project."""