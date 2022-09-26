import numpy as np
import pandas as pd
import math

data = [['Girev', 'Andrey', 'ВИП', 2815, 29, 58, 6358, 'Moscow', 'Xiaomi'],
        ['Bykin', 'Stas', 'Все за 300', 3634, 37, 78, 602, 'Kazan',
         'Samsung'],
        ['Ivanov', 'Alex', 'Всё за 800', 410, 47, 81, 3582, 'Moscow',
         'Huawei'],
        ['Andreev', 'Sergey', 'Всё за 500', 1981, 75, 98, 5442, 'Kazan',
         'Apple'],
        ['Girev', 'Stas', 'Всё за 800', 4969, 43, 61, 8510, 'Moscow',
         'Samsung'],
        ['Bykin', 'Andrey', 'Всё за 500', 4308, 49, 39, 2525, 'Moscow',
         'Xiaomi'],
        ['Kozlov', 'Igor', 'Всё за 800', 300, 60, 31, 8543, 'Yakutsk',
         'Samsung'],
        ['Girev', 'Alex', 'Промо', 4199, 47, 90, 3925, 'Kazan', 'Apple'],
        ['Petrov', 'Nikolay', 'ВИП', 4810, 72, 88, 7188, 'Moscow',
         'Apple'],
        ['Andreev', 'Sergey', 'Всё за 800', 4118, 52, 53, 419, 'Yakutsk',
         'Apple'],
        ['Smolov', 'Stas', 'Промо', 1991, 28, 67, 5016, 'Kazan', 'Xiaomi'],
        ['Girev', 'Igor', 'Корпоративный', 1430, 69, 19, 9520, 'Yakutsk',
         'Samsung'],
        ['Kozlov', 'Andrey', 'Корпоративный', 113, 71, 82, 2785, 'Kazan',
         'Apple'],
        ['Ivanov', 'Sergey', 'Промо', 3394, 39, 12, 2718, 'Yakutsk',
         'Xiaomi'],
        ['Smolov', 'Sergey', 'Всё за 250 (архив)', 3493, 32, 6, 8959,
         'Yakutsk', 'Huawei'],
        ['Kozlov', 'Stas', 'Всё за 800', 4565, 59, 82, 3168, 'Moscow',
         'Apple'],
        ['Vlasov', 'Andrey', 'Всё за 800', 3192, 29, 74, 2852, 'Yakutsk',
         'Xiaomi'],
        ['Smolov', 'Alex', 'Корпоративный', 3764, 71, 22, 2768, 'Moscow',
         'Huawei'],
        ['Vlasov', 'Sergey', 'Всё за 800', 3816, 28, 35, 5734,
         'Vladivostok', 'Apple'],
        ['Bykin', 'Alex', 'Промо', 817, 65, 34, 2131, 'Vladivostok',
         'Samsung'],
        ['Andreev', 'Nikolay', 'Всё за 500', 385, 49, 62, 1815, 'Kazan',
         'Xiaomi'],
        ['Bykin', 'Igor', 'Всё за 500', 2642, 38, 11, 3787, 'Moscow',
         'Xiaomi'],
        ['Girev', 'Sergey', 'Все за 300', 4230, 62, 68, 5512,
         'Vladivostok', 'Samsung'],
        ['Bykin', 'Sergey', 'Всё за 800', 4100, 48, 39, 227, 'Moscow',
         'Xiaomi'],
        ['Girev', 'Stas', 'Все за 300', 3371, 53, 24, 7946, 'Kazan',
         'Apple'],
        ['Smolov', 'Sergey', 'Корпоративный', 3577, 70, 71, 8847,
         'Yakutsk', 'Huawei'],
        ['Mezov', 'Nikolay', 'Всё за 250 (архив)', 2742, 28, 19, 7115,
         'Yakutsk', 'Huawei'],
        ['Smolov', 'Stas', 'Всё за 500', 2644, 41, 33, 8341, 'Moscow',
         'Xiaomi'],
        ['Vlasov', 'Andrey', 'Всё за 500', 4725, 26, 93, 9441,
         'Vladivostok', 'Xiaomi'],
        ['Ivanov', 'Nikolay', 'Всё за 500', 2785, 41, 5, 2901, 'Moscow',
         'Samsung']]

_df = pd.DataFrame(data, columns=['surname', 'name', 'tarif', 'balance', 'age', 'sms', 'voice', 'city', 'phone'])
# print(_df)

# # step 1
# _df["client_name"] = _df["surname"] + " " + _df["name"]
# print(_df)

# # step 2
# _df["group"] = np.where(_df["age"] <= 25, "A", np.where(_df["age"] > 40, "C", "B"))
# _df["group"] = np.where(_df["age"] <= 25, "A", _df["age"])
# _df["group"] = np.where(_df["age"] > 40, "C", "B")
# print(_df)

# # step 3
# _df["balance"] = np.where(_df["city"] == "Moscow", _df["balance"] - _df["sms"] * 3, _df["balance"])
# print(_df[["balance", "city"]])

# # step 4
# m1 = np.load("data.npz")
# print(m1['mykey1'])
# print(m1['mykey2'])
# print(m1.files)


# # step 5
# result = "mykey1"

# # step 6
# df_cost = pd.DataFrame(
#     {"tarif": ["ВИП", "Все за 300", "Всё за 500", "Всё за 800", "Промо", "Корпоративный", "Всё за 250 (архив)"],
#      "cost": [1, 2, 3, 4, 7, 0, 5]})
# result = _df.merge(df_cost, how="left", on="tarif")
# result["balance"] = np.where(result["city"] == "Moscow", result["balance"] - result["sms"] * result["cost"],
#                              result["balance"])
# result.drop("cost", axis=1, inplace=True)
# print(result[["balance", "city"]])

# # step 7
# _df.loc[(_df.surname == 'Girev') & (_df.name == 'Sergey') & (_df.city == 'Vladivostok'), 'city'] = 'Kazan'
# print(_df)

# # step 8
# _df.rename(columns={"balance": "client_balance"}, inplace=True)
# print(_df.iloc[:, [3, 4]])

# # step 9
# result = "argmin"

# # step 10
# _df["balance_usd"] = round(_df["balance"] / 60, 2)
# print(_df)

# # step 11
# _df["balance_usd"] = round(_df["balance"] / 60, 2)
# print(_df)

# # step 11
# _df["balance_usd"] = round(_df["balance"] / 60, 2)
# _df["balance_usd"] = _df["balance_usd"].astype(str)
# _df["balance_usd"] = _df["balance_usd"] + " $"
# print(_df["balance_usd"])

# # step 12
# _df["sms_volume"] = _df.sms / _df.sms.sum()
# _df.sort_values(by=["sms_volume"], ascending=False, inplace=True)
# result = _df.iloc[:3]
# print(result)

# # step 13
# df1 = _df.groupby("city").age.mean()
# print(df1["Kazan"] > df1["Vladivostok"])
#
# print(df1)

# # step 14
# result = "at"

# # step 15
# s1 = _df["surname"] + "_" + _df["name"]
# lst = [i.upper() for i in s1.values]
# _df.index = lst
# del _df["surname"], _df["name"]
# print(_df)

# # step 16
# s1 = pd.Series(_df.index)
# print(len(s1.unique()) == len(s1))
