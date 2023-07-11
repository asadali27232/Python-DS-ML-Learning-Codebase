import pandas as pd
import matplotlib.pyplot as plt

# Read 'homlessness.csv' into a DataFrame as homelessness
avocados = pd.read_csv("04_Data-Manipulation-with-pandas\Chapter4_Creating-and-Visualizing-DataFrames\\avocados.csv", index_col=0, header=0)

# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby("date").sum()["nb_sold"]

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(kind="line")

# Show the plot
plt.show()
