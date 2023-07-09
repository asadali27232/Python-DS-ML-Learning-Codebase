# Import pandas using the alias pd
import pandas as pd

# Read 'homlessness.csv' into a DataFrame as homelessness
homelessness = pd.read_csv("04_Data-Manipulation-with-pandas\Chapter1_Transforming-DataFrames\homelessness.csv", index_col=0, header=0)

# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness["individuals"] > 10000]
# See the result
print(ind_gt_10k)

# Filter for rows where region is Mountain
mountain_reg = homelessness[homelessness["region"] == "Mountain"]
# See the result
print(mountain_reg)

# Filter for rows where family_members is less than 1000 and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness["family_members"] < 1000) & (homelessness["region"] == "Pacific")]
# See the result
print(fam_lt_1k_pac)
