# Import pandas using the alias pd
import pandas as pd

# Read 'homlessness.csv' into a DataFrame as homelessness
homelessness = pd.read_csv("04_Data-Manipulation-with-pandas\Chapter1_Transforming-DataFrames\homelessness.csv", index_col=0, header=0)

# Subset for rows in South Atlantic or Mid-Atlantic regions
south_mid_atlantic = homelessness[homelessness["region"].isin(["South Atlantic", "Mid-Atlantic"])]
# See the result
print(south_mid_atlantic)

# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]
# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness["state"].isin(canu)]
# See the result
print(mojave_homelessness)
