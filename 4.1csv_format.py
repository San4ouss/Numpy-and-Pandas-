import pandas as pd
import numpy as np
import math

df = pd.read_csv("Пассажиропоток_МосМетро_2.csv", sep=";", skiprows=[1])

# print(df.columns)
# print(df.index)
# print(df.head())
# print(df[['NameOfStation', 'Year', 'Quarter', 'IncomingPassengers']])
df1 = df[(df['Year'] == 2021) & (df['Quarter'] == "IV квартал")][
    ['NameOfStation', 'Year', 'Quarter', 'IncomingPassengers']]
# print(df1[['NameOfStation', 'Year', 'Quarter', 'IncomingPassengers']])
print(df1.groupby("NameOfStation").IncomingPassengers.sum().idxmax())
