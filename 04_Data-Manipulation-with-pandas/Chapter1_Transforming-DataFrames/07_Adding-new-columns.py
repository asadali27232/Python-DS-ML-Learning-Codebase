# Import pandas using the alias pd
import pandas as pd

# Read 'homlessness.csv' into a DataFrame as homelessness
homelessness = pd.read_csv("04_Data-Manipulation-with-pandas\Chapter1_Transforming-DataFrames\homelessness.csv", index_col=0, header=0)

# Add total col as sum of individuals and family_members
homelessness["total"] = homelessness["individuals"] + homelessness["family_members"]

# Add p_individuals col as proportion of total that are individuals
homelessness["p_individuals"] = homelessness["individuals"] / homelessness["total"]

# See the result
print(homelessness)
