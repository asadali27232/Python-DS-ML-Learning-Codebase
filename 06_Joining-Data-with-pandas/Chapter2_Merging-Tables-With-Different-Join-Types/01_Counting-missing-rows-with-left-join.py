import pandas as pd

movies = pd.read_csv("movies.csv")
financials = pd.read_csv("financials.csv")

# Merge movies and financials with a left join
movies_financials = movies.merge(financials, how="left")

print(movies_financials.head())
