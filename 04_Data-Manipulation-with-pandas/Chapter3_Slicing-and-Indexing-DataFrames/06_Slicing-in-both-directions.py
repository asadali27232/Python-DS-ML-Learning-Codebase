import pandas as pd

# Read 'homlessness.csv' into a DataFrame as homelessness
temperatures = pd.read_csv("04_Data-Manipulation-with-pandas\Chapter3_Slicing-and-Indexing-DataFrames\\temperatures.csv", index_col=0, header=0)

# Index temperatures by country & city
temperatures_ind = temperatures.set_index(["country", "city"])

# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq", "Baghdad")])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:, "date":"avg_temp_c"])

# Subset in both directions at once
print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq", "Baghdad"), "date":"avg_temp_c"])
