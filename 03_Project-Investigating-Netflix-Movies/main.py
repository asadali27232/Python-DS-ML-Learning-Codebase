# Create the years and durations lists
years = [x for x in range(2011, 2021)]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

# Create a dictionary with the two lists
movie_dict = dict()
movie_dict["years"] = years
movie_dict["durations"] = durations

# Print the dictionary
movie_dict

# Import pandas under its usual alias
import pandas as pd

# Create a DataFrame from the dictionary
durations_df = pd.DataFrame(movie_dict)

# Print the DataFrame
print(durations_df)

# Import matplotlib.pyplot under its usual alias and create a figure
import matplotlib.pyplot as plt

fig = plt.figure()

# Draw a line plot of release_years and durations
plt.plot(durations_df.loc[:, "years"], durations_df.loc[:, "durations"])

# Create a title
plt.title("Netflix Movie Durations 2011-2020")

# Show the plot
plt.show()

# Read in the CSV as a DataFrame
netflix_df = pd.read_csv("03_Investigating-Netflix-Movies\\netflix_data.csv")

# Print the first five rows of the DataFrame
print(netflix_df.iloc[0:5, :])

# Subset the DataFrame for type "Movie"
netflix_df_movies_only = netflix_df[netflix_df["type"] == "Movie"]

# Select only the columns of interest
netflix_movies_col_subset = pd.DataFrame(netflix_df_movies_only.loc[:, ["title", "country", "genre", "release_year", "duration"]])

# Print the first five rows of the new DataFrame
print(netflix_movies_col_subset.iloc[0:5, :])

# Create a figure and increase the figure size
fig = plt.figure(figsize=(12, 8))

# Create a scatter plot of duration versus year
plt.scatter(netflix_movies_col_subset["release_year"], netflix_movies_col_subset["duration"])

# Create a title
plt.title("Movie Duration by Year of Release")

# Show the plot
plt.show()


# Filter for durations shorter than 60 minutes
short_movies = netflix_movies_col_subset[netflix_movies_col_subset["duration"] < 60]

# Print the first 20 rows of short_movies
print(short_movies.iloc[0:20, :])

# Define an empty list
colors = list()

# Iterate over rows of netflix_movies_col_subset
for label, row in netflix_movies_col_subset.iterrows():
    if row["genre"] == "Children":
        colors.append("red")
    elif row["genre"] == "Documentaries":
        colors.append("blue")
    elif row["genre"] == "Stand-Up":
        colors.append("green")
    else:
        colors.append("black")

# Inspect the first 10 values in your list
print(netflix_movies_col_subset.iloc[0:10, :])

# Set the figure style and initalize a new figure
plt.style.use("fivethirtyeight")
fig = plt.figure(figsize=(12, 8))

# Create a scatter plot of duration versus release_year
plt.scatter(netflix_movies_col_subset["release_year"], netflix_movies_col_subset["duration"], c=colors)

# Create a title and axis labels
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.title("Movie duration by year of release")

# Show the plot
plt.show()

# Are we certain that movies are getting shorter?
are_movies_getting_shorter = "maybe"