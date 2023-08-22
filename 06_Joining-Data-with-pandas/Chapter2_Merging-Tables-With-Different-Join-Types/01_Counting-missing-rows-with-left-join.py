import pandas as pd

movies = pd.read_csv("movies.csv")
financials = pd.read_csv("financials.csv")

# Merge movies and financials with a left join
movies_financials = movies.merge(financials, on="id", how="left")

# Count the number of rows in the budget column that are missing
number_of_missing_fin = movies_financials['budget'].isnull().sum()

# Print the number of movies missing financials
print(number_of_missing_fin)