import pandas as pd

with open("users1.csv", encoding="utf-8") as f:
    file = f.read()
    # print(file)

df = pd.read_csv("users1.csv", sep=";")
print(df.columns)
df2 = df[df["sex"] == "F"]
# print(df2[["username", "mail"]])
df2.to_csv("users_name_mail.csv", encoding="utf-8", sep=";", columns=["username", "mail"], index=False)
