import pandas as pd

with open("users2.csv", encoding="utf-8") as f:
    file = f.read()
    # print(file)

df = pd.read_csv("users2.csv", sep=";", nrows=50)
df2 = df[df["sex"] == "M"]
# print(df2["sex"])
print(df2.count())
