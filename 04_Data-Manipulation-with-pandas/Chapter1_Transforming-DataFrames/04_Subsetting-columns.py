# Import pandas using the alias pd
import pandas as pd

# Read 'homlessness.csv' into a DataFrame as homelessness
homelessness = pd.read_csv("04_Data-Manipulation-with-pandas\Chapter1_Transforming-DataFrames\homelessness.csv", index_col=0, header=0)

# Select the individuals column
individuals = homelessness["individuals"]

# Print the head of the result
print(individuals.head())

# Select the state and family_members columns
state_fam = homelessness[["state", "family_members"]]

# Print the head of the result
print(state_fam.head())

# Select only the individuals and state columns, in that order
ind_state = homelessness[["individuals", "state"]]

# Print the head of the result
print(ind_state.head())
