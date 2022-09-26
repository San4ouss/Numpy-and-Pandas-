import pandas as pd

# with open("users4.csv", encoding="utf-8") as f:
#     file = f.read()
#     print(file)

df = pd.read_csv("users4.csv", sep=";")
# print(df.columns)
df[["username", "name", "sex"]].to_json("users4.json")
