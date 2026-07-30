import pandas as pd

# Load dataset
df = pd.read_csv("insurance.csv")

# 5a: Create DataFrame
print("First 5 rows of Dataset:")
print(df.head())

print("\nShape of Dataset:")
print(df.shape)


# 5b: Statistical Information
print("\nStatistical Information:")
print(df.describe())

print("\nDataset Information:")
df.info()


# 5c: Create Pandas Series from Dictionary
data = dict(df.iloc[0])
s = pd.Series(data)

print("\nPandas Series:")
print(s)


# 5d: Filter Pandas Series using Boolean Array
series = pd.Series(df.iloc[:, 0])

print("\nOriginal Series:")
print(series)
PRINT("KRISH GUPTA 085")

print("\nFiltered Values:")
print(series[series > 15])
