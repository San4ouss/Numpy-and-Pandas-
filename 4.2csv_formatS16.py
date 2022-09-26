import pandas as pd
import numpy as np
import math

# with open("Пассажиропоток_МосМетро_4.csv", encoding="utf-8") as f:
#     file = f.read()
#     print(file)
#     lst = file.split("\n")
#     for i, j in enumerate(lst):
#         if "#" in j or "/" in j or "не указано" in j or "NULL" in j or "None" in j:
#             print(j)

df = pd.read_csv("Пассажиропоток_МосМетро_4.csv", sep="|", skiprows=[1],
                 na_values={"IncomingPassengers": [0, "NULL", "None", "не указано"],
                            "OutgoingPassengers": ["NULL", "None", "не указано"]})
# print(df.columns)
# print(df[['NameOfStation', 'IncomingPassengers', 'OutgoingPassengers']])
print(len(df[pd.isnull(df["IncomingPassengers"])]))
