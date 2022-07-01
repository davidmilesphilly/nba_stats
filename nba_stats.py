import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn import utils
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.read_csv('Players.csv')
df1 = pd.read_csv('player_data.csv')
df2 = pd.read_csv('seasons_stats.csv')

df.rename(columns = {'collage':'college'}, inplace = True)
new_df2 = df2.loc[(df2['G'] > 40) & (df2['Year'] >= 1990)]
new_df2 = new_df2.drop('Unnamed: 0', 1)


# Clean up dataset



# Add new columns
new_df2['MPG'] = new_df2['MP'] / new_df2['G']
new_df2['PPG'] = new_df2['PTS'] / new_df2['G']
new_df2['RPG'] = new_df2['TRB'] / new_df2['G']
new_df2['SPG'] = new_df2['STL'] / new_df2['G']
new_df2['BPG'] = new_df2['BLK'] / new_df2['G']
new_df2['APG'] = new_df2['AST'] / new_df2['G']
df3 = new_df2.loc[(new_df2['G'] > 40) & (new_df2['Year'] >= 1980)]
df3 = df3.drop(columns = ['blank2', 'blanl'])
df3 = df3.round(decimals=2)
##########################################################################
# print(df3.columns)


# Create player_grp for player stats
player_grp = df3.groupby(['Player'])
# print(player_grp.get_group('Kobe Bryant').agg(['mean', 'sum', 'max', 'median']))
#########################################################################

# Best individual TS%/best TS% career (min 6 yeared played)
# (min 12 points a game)

# print(df3.loc[player_grp,['TS%']])
# print(df3.loc[player_grp, df3['TS%']])
filtera = (df3['PPG'] > 14)
filterb = (df3['MPG'] < 20) & (df3['PPG'] > 7) & (df3['Pos'] == 'SF')
filterc = (df3['Player'] == 'Monty Williams')
player_years = df3.loc[filterc, ['Player', 'Tm', 'Pos', 'Year', 'TS%', 'PPG', 'MPG', 'SPG', 'APG', 'BPG', 'FG%']].sort_values(by = ('Year'), ascending = True).head(20)
# print(player_years)
# ts_data = df3.loc[filterb, ['Player', 'Tm', 'Pos', 'Year', 'TS%', 'PPG', 'MPG', 'SPG', 'BPG', 'FG%']].sort_values(by = ('TS%'), ascending = False).head(20)
# print(ts_data)
# print(df3.sort_values(['TS%']))
# best_ts = df3.loc[player_grp, ['TS%']]
# print(best_ts)
# Best players season/career ts% while averaging less than 20 ppg


# def team(x):
#     if x is df3['Player']:
#         return df3['Tm']

king = df3.Player('Lebron James')
print(king)
