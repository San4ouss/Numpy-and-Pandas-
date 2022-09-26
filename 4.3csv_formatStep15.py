import pandas as pd

with open("users3.csv", encoding="utf-8") as f:
    file = f.read()
    # print(file)

df = pd.read_csv("users3.csv", sep=";", chunksize=30)
for i in range(4):
    next(df)

df2 = next(df)
print(len(df2[df2["blood_group"] == "A+"]))
