import pandas as pd

df1 = pd.read_excel("trekking2.xlsx", sheet_name=0, index_col=0).fillna(0)
df2 = pd.read_excel("trekking2.xlsx", sheet_name=1, index_col=0)
df2_new = pd.DataFrame()
df2_new["ККал на 100"] = df2["Вес в граммах"]
df2_new["Б на 100"] = df2["Вес в граммах"]
df2_new["Ж на 100"] = df2["Вес в граммах"]
df2_new["У на 100"] = df2["Вес в граммах"]

result = df1 / 100 * df2_new

# print(result.sum().astype(int))

for i in result.sum():
    print(int(i), end=" ")
