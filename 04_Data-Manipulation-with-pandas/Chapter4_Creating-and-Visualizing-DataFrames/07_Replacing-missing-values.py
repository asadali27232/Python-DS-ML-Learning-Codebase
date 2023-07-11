import pandas as pd
import matplotlib.pyplot as plt

# Read 'dirty_avocados.csv' into a DataFrame as homelessness
avocados_2016 = pd.read_csv("04_Data-Manipulation-with-pandas\Chapter4_Creating-and-Visualizing-DataFrames\dirty_avocados.csv", index_col=0, header=0)

# From previous step
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
avocados_2016[cols_with_missing].hist()
plt.show()

# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)

# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()

# Show the plot
plt.show()
