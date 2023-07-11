import pandas as pd
import matplotlib.pyplot as plt

# Read 'homlessness.csv' into a DataFrame as homelessness
avocados_2016 = pd.read_csv("04_Data-Manipulation-with-pandas\Chapter4_Creating-and-Visualizing-DataFrames\dirty_avocados.csv", index_col=0, header=0)

# Check individual values for missing values
print(avocados_2016.isna())

# Check each column for missing values
print(avocados_2016.isna().any())

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind="bar")

# Show plot
plt.show()
