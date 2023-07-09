import pandas as pd

# Read 'homlessness.csv' into a DataFrame as homelessness
homelessness = pd.read_csv("04_Data-Manipulation-with-pandas\Chapter1_Transforming-DataFrames\homelessness.csv", index_col=0, header=0)

# Print the head of the homelessness data
print(homelessness.head())

# Print information about homelessness
print(homelessness.info())

# Print the shape of homelessness
print(homelessness.shape)

# Print a description of homelessness
print(homelessness.describe())
