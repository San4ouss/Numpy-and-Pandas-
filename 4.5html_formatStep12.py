import pandas as pd

lst = pd.read_html("23110000100100200001_Общий_прирост_постоянного_населения.html", skiprows=[0, 1], index_col=0)
df = lst[0].fillna(0)
# print(df.columns)
# print(df.index)
s1 = df.loc["Камчатский край"]
years = [j for i in s1.index
         for j in i.split()
         if j.isdigit()]
s1.index = years
right_years = [str(i) for i in range(2014, 2021)]
print(int(s1.loc[right_years].sum()))
