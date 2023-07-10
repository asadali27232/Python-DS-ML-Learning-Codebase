import pandas as pd

# Read 'homlessness.csv' into a DataFrame as homelessness
temperatures = pd.read_csv("04_Data-Manipulation-with-pandas\Chapter3_Slicing-and-Indexing-DataFrames\\temperatures.csv", index_col=0, header=0)

# Convert "date" column to datetime data type
temperatures["date"] = pd.to_datetime(temperatures["date"])

# Add a year column to temperatures
temperatures["year"] = temperatures["date"].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table(values="avg_temp_c", index=["country", "city"], columns="year")

# See the result
print(temp_by_country_city_vs_year)
