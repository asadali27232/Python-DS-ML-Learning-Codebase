import pandas as pd
import matplotlib.pyplot as plt

# Read 'avocados.csv' into a DataFrame as homelessness
avocados = pd.read_csv("04_Data-Manipulation-with-pandas\Chapter4_Creating-and-Visualizing-DataFrames\\avocados.csv", index_col=0, header=0)

# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.set_index("size").pivot_table(values="nb_sold", index="size", aggfunc=sum)
print(nb_sold_by_size)

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind="bar")

# Show the plot
plt.show()
