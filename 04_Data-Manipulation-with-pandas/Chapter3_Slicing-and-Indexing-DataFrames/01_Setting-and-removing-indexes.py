import pandas as pd

# Read 'temperatures.csv' into a DataFrame as homelessness
temperatures = pd.read_csv("04_Data-Manipulation-with-pandas\Chapter3_Slicing-and-Indexing-DataFrames\\temperatures.csv", index_col=0, header=0)

# Look at temperatures
print(temperatures)

# Set the index of temperatures to city
temperatures_ind = temperatures.set_index("city")

# Look at temperatures_ind
print(temperatures_ind)

# Reset the temperatures_ind index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the temperatures_ind index, dropping its contents
print(temperatures_ind.reset_index(drop=True))
