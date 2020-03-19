import pandas as pd
import numpy as np
import os

df = pd.read_csv("wildlife-strike-2006-2015.csv", header= 0 , sep=",")

print("\nColumns:")
print(df.columns)
print("\nIndex:")
print(df.index)
print("\nDataType:")
print(df.dtypes)
print("\nShape:")
print(df.shape)
print("\nInfo:")
print(df.info())
print("\nDescribe:")
print(df['Incident Year'].describe())

print("\nCorrelation matrix")
print(df.corr())

# 8. Cause of accidents
print("\nGroup by Flight Phase info:")
print(df.groupby('Flight Phase').count())

print("\nGroup by Warning Issued info:")
print(df.groupby('Warning Issued').count())

print("\nGroup by Flight Impact info:")
print(df.groupby('Flight Impact').count())
