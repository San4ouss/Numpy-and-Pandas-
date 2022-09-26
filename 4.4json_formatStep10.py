import pandas as pd

# with open("data-399-2022-07-01.json", encoding="Windows-1251") as f:
#     file = f.read()
#     print(file)

df = pd.read_json("data-399-2022-07-01.json", encoding="Windows-1251")
# print(df.columns)
print(df[df["TicketCost"] == df["TicketCost"].min()]["NameOfTariff"])
