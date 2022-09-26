import sqlalchemy as sql

import pandas as pd

con = sql.create_engine("sqlite:///local_db.db")
df = pd.read_sql("SELECT Name, StationCapacity, Location FROM stations GROUP BY Name, Location", con)
df["StationCapacity"] = df["StationCapacity"].astype(int)
# print(df.dtypes)
df.sort_values(by=["StationCapacity", "Name"], ascending=[False, True], inplace=True)
# df.to_csv("stations.csv", sep=";", index=False, encoding="utf-8")
print(df[["Name", "StationCapacity"]])
