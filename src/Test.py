import pandas as pd
from pandas import DataFrame

df: DataFrame = pd.read_csv('emails.csv')
print(type(df))
print(df)
