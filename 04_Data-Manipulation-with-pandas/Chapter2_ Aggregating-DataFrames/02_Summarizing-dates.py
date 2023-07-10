# Import pandas using the alias pd
import pandas as pd

# Read 'homlessness.csv' into a DataFrame as homelessness
sales = pd.read_csv("04_Data-Manipulation-with-pandas\Chapter2_ Aggregating-DataFrames\sales.csv", index_col=0, header=0)

# Print the maximum of the date column
print(sales["date"].max())

# Print the minimum of the date column
print(sales["date"].min())
