import pandas as pd

df_guide = pd.read_excel("trekking3.xlsx", sheet_name=0).fillna(0)
df_guide.rename(columns={'Unnamed: 0': 'Продукт'}, inplace=True)

df_days = pd.read_excel("trekking3.xlsx", sheet_name=1)
# print(df_guide)
# print(df_days)
# print(df_guide.columns)
# print(df_days.columns)

df = df_guide.merge(df_days, how="inner", on="Продукт")
df["ККал на 100"] = df["ККал на 100"] / 100 * df["Вес в граммах"]
df["Б на 100"] = df["Б на 100"] / 100 * df["Вес в граммах"]
df["Ж на 100"] = df["Ж на 100"] / 100 * df["Вес в граммах"]
df["У на 100"] = df["У на 100"] / 100 * df["Вес в граммах"]

result = df.groupby("День").sum().astype(int)
result.drop("Вес в граммах", axis=1, inplace=True)

for i in result.values:
    print(*i)
