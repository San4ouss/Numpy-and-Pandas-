import pandas as pd
import numpy as np
import math

data = pd.read_excel('salaries.xlsx', sheet_name=0, index_col="Unnamed: 0")
# print(data.median(axis=1).idxmax(), data.mean(axis=0).idxmax())
print(data)
