import pandas as pd

store = pd.HDFStore('data_store2.h5')
# print(store.keys())
df = pd.DataFrame(store.select("parking_table"), columns=["District", "Capacity"])
print(df[df["District"] == "район Тропарёво-Никулино"].sum())
