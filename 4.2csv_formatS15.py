import pandas as pd
import numpy as np
import math

# находим коварный комментарий
with open("Пассажиропоток_МосМетро_3.csv", encoding="utf-8") as f:
    file = f.read()
    lst = file.split("\n")
    skip_lst = []
    for i, j in enumerate(lst):
        if "//Ха-ха тут закрался коварный комментарий." in j or "#" in j or "Станция метрополитена" in j:
            skip_lst.append(i)

    # print(file)
    # print(len(lst))
    # print(lst)
    # print(lst[1380])

df = pd.read_csv("Пассажиропоток_МосМетро_3.csv", sep="|", skiprows=skip_lst)
# print(df.columns)
# print(df.groupby("NameOfStation").IncomingPassengers.sum())
print(df["IncomingPassengers"].sum())
