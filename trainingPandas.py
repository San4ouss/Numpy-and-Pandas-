import pandas as pd
import numpy as np
import statistics

# s1 = pd.Series([4, 3, -7, 5])
# print(s1)

# s2 = pd.Series([4, 3, -7, 5], index=["a", "b", "c", "d"])
# print(s2)

# arr1 = np.arange(6).reshape((2, 3))
# print(arr1)
# result = pd.Series(arr1)
# print(result)

# s1 = pd.Series([1, 2, 3, 4], index=["a", "d", "e", "f"])
# s2 = pd.Series([4, 3, 7, 5], index=["a", "b", "c", "d"])
# s3 = s2[s2 > 4]
# print(s3.index)
# print(s1 + s2)
# s4 = pd.Series([4, 3, 3, 5], index=["a", "d", "e", "f"])
# print(s1 == s4)

# d = {"Moscow": 1400, "Murmansk": 900, "Kazan": 200}
# s3 = pd.Series(d, index=["Kazan", "Moscow1", "Murmansk"])
# s4 = pd.Series(d, index=["Moscow"])
# print(s3)
# print(s4)

# s1 = pd.Series([-1, 2, 3, -5])
# s1.index = ["a", "b", "c", "d"]
# print(s1.index)
# s1.index.name = "index1"
# print(s1)
# print(s1[s1 > 3])

# print(s1.index[::-1])
# s1.index = sorted(s1.index, reverse=True)
# print(s1)

# df = pd.DataFrame()
# print(df)

# s1 = pd.Series(["Ivan", "Andrew", "Igor"])
# s1.name = "user_names"
# df = pd.DataFrame(s1)
# print(df)
# print(df["user_names"])

# data = {"city": ["Moscow", "Moscow", "Moscow", "Kazan", "Kazan", "Kazan"],
#         "year": [2022, 2021, 2020, 2022, 2021, 2020],
#         "visits": [500, 2000, 1500, 100, 230, 200]}
# #
# df = pd.DataFrame(data, index=["a", "b", "c", "d", "e", "f"])
# print(df)
# print(df.values)
# print(df.head(2))
# print(df["city"])
# print(df.city)
# print(df.loc["b":"d"])
# df.index = range(6)
# df.balance = [500, 2000, 1500, 100, 230, 200]
# print(df)
# print(df["city"]["b"])
# print(df.reindex(["city", "visits"]))
# print(df.reindex(["city", "visits"], axis=1))

# labels = [i.upper() for i in df.columns]
# print(labels)
# df.columns = labels
# print(df.columns)
# print(df.shape)

# df2 = pd.DataFrame(data, columns=["visits", "city"])
# print(df2)
# print(df2.loc[0:2])

# s1 = pd.Series([1, 2, 3], index=["a", "b", "c"])
# labels = s1.index
# s2 = pd.Series([5, 6, 7], index=labels)
# print(s2)
# s1.index = range(3)
# print(s1)

# df1 = pd.DataFrame([1, 2, 3], index=[0, 1, 2])
# df2 = pd.DataFrame([3, 4, 5], index=["a", "b", "c"])
# print(df1 + df2)
# print(df1.T)

# s1 = pd.Series([1, 2, 3], index=[0, 1, 2])
# s2 = pd.Series([4, 5, 6], index=["a", "b", "c"])
# print(s1 + s2)
# s1.name = "first"
# print(s1.T)

# data = {"user_name": ["Ivan", "Alex", "Ugen"],
#         "clicks": [2, 5, 8],
#         "time_interval": [3, 6, 9]}
# df = pd.DataFrame(data, index=[0, 1, 2])
# df.T
# print(df.index)
# df1 = df.T
# print(df1.index)

# df = pd.DataFrame(np.arange(16).reshape((4, 4)), index=["Moscow", "Vladivostok", "Ufa", "Kazan"],
#                   columns=["col_1", "col_2", "col_3", "col_4"])
# print(df)
# print(df[["col_1", "col_4"]])
# print(df[:2])
# print(df["col_3"] > 9)
# print(df[df["col_3"] > 9])
# print(df < 10)
# df[df < 10] = 0
# print(df)
# r = df.reindex(["Moscow"])
# print(r[["col_1", "col_2"]])

# data = [['Ivan', 25, 4, 50, 1],
#
#         ['Petr', 40, 9, 250, 8],
#
#         ['Nikolay', 19, 12, 25, 1],
#
#         ['Sergey', 33, 6, 115, 6],
#
#         ['Andrey', 38, 2, 152, 4],
#
#         ['Ilya', 20, 18, 15, 2],
#
#         ['Igor', 19, 2, 10, 1]]
#
# _df = pd.DataFrame(data, columns=['name', 'age', 'clicks', 'balance', 'history'], index=list('abcdefg'))

# r = _df[_df["age"] < 30]
# result = r[r["balance"] > 20]
# result = _df[(_df["age"] < 30) & (_df["balance"] > 20)]
# print(result)

# result = _df[_df["balance"] > 100][["name", "age"]]
# print(result)

# result = _df[(_df["name"] == "Petr") | (_df["name"] == "Andrey")][['name', 'age', 'balance']]
# print(result)

# arr1 = np.array(_df["balance"])
# arr1[arr1 < 100] = 0
# _df["balance"] = arr1
# print(arr1)
# print(_df)

# data = [['Ivan', 25, 4, 50, 1],
#
#         ['Petr', 40, 9, 250, 8],
#
#         ['Nikolay', 19, 12, 25, 1],
#
#         ['Sergey', 33, 6, 115, 6],
#
#         ['Andrey', 38, 2, 152, 4],
#
#         ['Ilya', 20, 18, 15, 2],
#
#         ['Igor', 19, 2, 10, 1]]
#
# _df = pd.DataFrame(data, columns=['user_name', 'user_age', 'user_clicks', 'user_balance', 'user_history'],
#                    index=list('abcdefg'))

# _df.columns = [i.lstrip("user_") for i in _df.columns]
# _df = _df.reindex([i.lstrip("user_") for i in _df.columns], axis=1)
# print(_df)

lst = [5, 4, 20, 4, 2, 7, 6, 4]
print(sorted(lst))
print(sum(lst)/len(lst))
print(np.median(lst))
# print(np.mod(lst))

print("xxxxxxxxxx")
print(statistics.mean(lst))
print(statistics.median(lst))
print(statistics.mode(lst))
