import pandas as pd

# Read 'temperatures.csv' into a DataFrame as homelessness
temperatures = pd.read_csv("04_Data-Manipulation-with-pandas\Chapter3_Slicing-and-Indexing-DataFrames\\temperatures.csv", index_col=0, header=0)

# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[22, 1])

# Use slicing to get the first 5 rows
print(temperatures.iloc[0:5])

# Use slicing to get columns 3 to 4
print(temperatures.iloc[:, 2:5])

# Use slicing in both directions at once
print(temperatures.iloc[:6, 2:5])
