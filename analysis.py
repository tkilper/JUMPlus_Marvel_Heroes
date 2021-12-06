# JUMPlus Data Project 2: Marvel Heroes
# Author: Tristan Kilper

# 1) Import libraries
print('1) Import required libraries')
print('--------------------------------------------------')
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
print('Python libraries pandas, numpy, seaborn, and matplotlib imported to file!')
print(' ')

# 2) Read csv
print('2) Read csv')
print('--------------------------------------------------')
df = pd.read_csv('C:/Users/Tristan Kilper/Desktop/JUMP/JUMPlus/Project2MarvelHeroes/JUMPlus_Marvel_Heroes/charcters_stats.csv')
print('csv read!')
print(' ')

# 3) Show first records
print('3) Show first records')
print('--------------------------------------------------')
print(df.head(10))
print(' ')

# 4) Show number of rows and columns
print('4) Show number of rows and columns')
print('--------------------------------------------------')
print(f'Number of rows in dataset: {len(df)}')
print(f'Number of columns in dataset: {len(df.columns)}')
print(' ')

# 5) You need to find the values of alignment, can use value_counts()
print('5) You need to find the values of alignment, can use value_counts()')
print('--------------------------------------------------')
print(df['Alignment'].value_counts())
print(' ')

# 6) Find out only good alignment holders superheroes
print('6) Find out only good alignment holders superheroes')
print('--------------------------------------------------')
print(df[df['Alignment'] == 'good'])
print(' ')

# 7) Show first five records which you found in point 6
print('7) Show first five records which you found in point 6')
print('--------------------------------------------------')
print(df[df['Alignment'] == 'good'].head(5))
print(' ')

# 8) Show top five records having top speed of heroes of good alignment
print('8) Show top five records having top speed of heroes of good alignment')
print('--------------------------------------------------')
print(df[df['Alignment'] == 'good'].sort_values(['Speed'], ascending=False).head(5))
print(' ')

# 9) Show 5 records of super heroes who have maximum power of good alignment
print('9) Show 5 records of super heroes who have maximum power of good alignment')
print('--------------------------------------------------')
print(df[df['Alignment'] == 'good'].sort_values(['Power'], ascending=False).head(5))
print(' ')

# 10) Find out how many super heroes are there with power 100 of good alignment
print('10) Find out how many super heroes are there with power 100 of good alignment')
print('--------------------------------------------------')
print(df[df['Alignment'] == 'good'].value_counts(['Power'] == 100))
print(' ')

# 11) Shape them what you got in point 10
print('11) Shape them what you got in point 10')
print('--------------------------------------------------')
print(' ')

# 12) Show all records from point 10
print('12) Show all records from point 10')
print('--------------------------------------------------')
print(' ')

# 2) Read csv
print('2) Read csv')
print('--------------------------------------------------')
print(' ')

# 2) Read csv
print('2) Read csv')
print('--------------------------------------------------')
print(' ')

# 2) Read csv
print('2) Read csv')
print('--------------------------------------------------')
print(' ')

# 2) Read csv
print('2) Read csv')
print('--------------------------------------------------')
print(' ')

# 2) Read csv
print('2) Read csv')
print('--------------------------------------------------')
print(' ')

# 2) Read csv
print('2) Read csv')
print('--------------------------------------------------')
print(' ')

# 2) Read csv
print('2) Read csv')
print('--------------------------------------------------')
print(' ')

# 2) Read csv
print('2) Read csv')
print('--------------------------------------------------')
print(' ')

# 2) Read csv
print('2) Read csv')
print('--------------------------------------------------')
print(' ')

# Bonus
print('BONUS')
print('--------------------------------------------------')
print(' ')