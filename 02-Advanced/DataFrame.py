import pandas as pd
import numpy as np
import os

# 1. Load the insurance.csv in a DataFrame using pandas.
# Explore the dataset using functions like to_string(), columns, index, dtypes, shape, info() and describe()

df = pd.read_csv("data/insurance.csv", header= 0 , sep=",")

print("\nColumns:")
print(df.columns)
print("\nIndex:")
print(df.index)
print("\nDataType:")
print(df.dtypes)
print("\nShape:")
print(df.shape)
print("\nTo string:")
print(df.to_string())
print("\nInfo:")
print(df.info())
print("\nDescribe:")
print(df.describe())

# 2. Print only the column age
print("\nPrint age column:")
print(df['age'].to_string())

# 3. Print only the columns age,children and charges
print("\nPrint columns age, children and charges:")
print(df[['age','children','charges']].to_string())

# 4. Print only the first 5 lines and only the columns age,children and charges
print("\nPrint first 5 lines age, children and charges:")
print(df[['age','children','charges']].head(6))

# 5. What is the average, minimum and maximum charges
print("\nPrint charges info:")
print(df['charges'].max())
print(df['charges'].min())
print(df['charges'].mean())

# 6. What is the age and sex of the person that paid 10797.3362. Was he/she a smoker?
print("\nPrint person paid 10797.3362:")
print(df.loc[df['charges'] == 10797.3362])

# 7. What is the age of the person who paid the maximum charge
print("\nPrint person paid max charge")
print(df.loc[df['charges'] == df['charges'].max()])

# 8. How many insured people do we have for each region
print("\nPrint region info:")
print(df.groupby('region').count())

# 9. How many insured people are children?
print("\nInsured children")
print(df['children'].sum())

# 10. What do you expect to be the correlation between charges and age, bmi and children?
# Charges increases with age
# BMI increases with children

# 11. Using the method corr(), check if your assumptions were correct.
print("\nCorrelation matrix")
print(df.corr())