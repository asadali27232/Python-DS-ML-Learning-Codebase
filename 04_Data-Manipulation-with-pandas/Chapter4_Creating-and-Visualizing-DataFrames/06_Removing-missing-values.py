import pandas as pd

# Read 'dirty_avocados.csv' into a DataFrame as homelessness
avocados_2016 = pd.read_csv("04_Data-Manipulation-with-pandas\Chapter4_Creating-and-Visualizing-DataFrames\dirty_avocados.csv", index_col=0, header=0)

# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())
