import pandas as pd

df = pd.read_excel("trekking1.xlsx", sheet_name=0).fillna(0)
df.rename(columns={"Unnamed: 0": "city"}, inplace=True)
# print(df.columns)
df.sort_values(by=["ККал на 100", "city"], ascending=[False, True], inplace=True)
# print(df["city"])
for i in df["city"]:
    print(i)
