import pandas as pd
import matplotlib.pyplot as plt

# Read 'avocados.csv' into a DataFrame as homelessness
avocados = pd.read_csv("04_Data-Manipulation-with-pandas\Chapter4_Creating-and-Visualizing-DataFrames\\avocados.csv", index_col=0, header=0)

# Modify bins to 20
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5, bins=20)

# Modify bins to 20
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5, bins=20)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()
