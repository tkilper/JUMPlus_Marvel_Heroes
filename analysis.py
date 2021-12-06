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
good_heroes = df[df['Alignment'] == 'good']
ghw100p = good_heroes[good_heroes['Power'] == 100]
print(len(ghw100p))
print(' ')

# 11) Shape them what you got in point 10
print('11) Shape them what you got in point 10')
print('--------------------------------------------------')
print(' ')

# 12) Show all records from point 10
print('12) Show all records from point 10')
print('--------------------------------------------------')
print(ghw100p)
print(' ')

# 13) Retrieve total of first five records of max power of good alignment super heroes
print('13) Retrieve total of first five records of max power of good alignment super heroes')
print('--------------------------------------------------')
print(ghw100p.head(5))
print(' ')

# 14) Draw a bar plot of all super heroes who are having good alignment and max power of top five only , take same object of point 13 , show name and total in plot with green bars
print('14) Draw a bar plot of all super heroes who are having good alignment and max power of top five only , take same object of point 13 , show name and total in plot with green bars')
print('--------------------------------------------------')

print(' ')

# 15) Extract villains having bad alignment
print('15) Extract villains having bad alignment')
print('--------------------------------------------------')
vils = df[df['Alignment'] == 'bad']
print(vils)
print(' ')

# 16) Show first five records of point 15
print('16) Show first five records of point 15')
print('--------------------------------------------------')
print(df[df['Alignment'] == 'bad'].head(5))
print(' ')

# 17) Show top five fastest super villains in terms of super speed
print('17) Show top five fastest super villains in terms of super speed')
print('--------------------------------------------------')
print(vils.sort_values(['Speed'], ascending=False).head(5))
print(' ')

# 18) Top five super villains in terms of intelligence
print('18) Top five super villains in terms of intelligence')
print('--------------------------------------------------')
print(vils.sort_values(['Intelligence'], ascending=False).head(5))
print(' ')

# 19) Show who is most dangerous super villain after calculating their total (top 5 only)
print('19) Show who is most dangerous super villain after calculating their total (top 5 only)')
print('--------------------------------------------------')
print(' ')

# 20) Draw a histogram for speed of super heroes having fig size 10,5 , provide speed in histogram for only good alignment super heroes ,title should be "distribution of speed" , xlabel should be "speed"
print('20) Draw a histogram for speed of super heroes having fig size 10,5 , provide speed in histogram for only good alignment super heroes ,title should be "distribution of speed" , xlabel should be "speed"')
print('--------------------------------------------------')
print(' ')

# 21) Draw a histogram for combat of super villains having fig size 10,5 , provide combat in histogram for only bad alignment super heroes ,title should be "distribution of combat" , xlabel should be "combat"
print('21) Draw a histogram for combat of super villains having fig size 10,5 , provide combat in histogram for only bad alignment super heroes ,title should be "distribution of combat" , xlabel should be "combat"')
print('--------------------------------------------------')
print(' ')