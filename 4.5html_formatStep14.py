import pandas as pd

lst = pd.read_html("23110000100100200001_Общий_прирост_постоянного_населения.html", skiprows=[0, 1, 3, 4], index_col=0)
df = lst[0].fillna(0)
# print(df.columns)
years = [j for i in df.columns
         for j in i.split()
         if j.isdigit()]
df.columns = years
df1 = df.groupby(df.index).sum()
s1 = df1["2020"].iloc[:, 0]
mask = ['Свердловская область', 'Магаданская область', 'Сахалинская область', 'Калужская область',
        'Ярославская область', 'Кировская область']
print(s1.loc[mask].idxmin())
