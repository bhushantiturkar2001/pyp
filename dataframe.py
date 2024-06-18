import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Writing DataFrame to a CSV file
df.to_csv('people.csv', index=False)

# Reading from a CSV file
df_read = pd.read_csv('people.csv')
print("\nDataFrame read from CSV:\n", df_read)

# DataFrame Methods
print("\nDataFrame Head:\n", df.head())
print("\nDataFrame Description:\n", df.describe())
print("\nDataFrame Info:\n", df.info())
