import pandas as pd
import matplotlib.pyplot as plt

# Read 'homlessness.csv' into a DataFrame as homelessness
avocados = pd.read_csv("04_Data-Manipulation-with-pandas\Chapter4_Creating-and-Visualizing-DataFrames\\avocados.csv", index_col=0, header=0)

# Scatter plot of avg_price vs. nb_sold with title
avocados.plot(x="nb_sold", y="avg_price", kind="scatter", title="Number of avocados sold vs. average price")

# Show the plot
plt.show()
