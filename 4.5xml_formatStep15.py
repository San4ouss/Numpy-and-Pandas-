import pandas as pd

df = pd.read_xml("users.xml")
# print(df.columns)
df1 = df[(df["sex"] == "F") & (df["blood_group"] == "B+")]
# print(df1.count())
print(len(df1))
