import pandas as pd

taxi_owners = pd.read_csv("taxi_owners.csv", index_col=0, header=0)
taxi_veh = pd.read_csv("taxi_veh.csv", index_col=0, header=0)

# Merge the taxi_owners and taxi_veh tables
taxi_own_veh = taxi_owners.merge(taxi_veh, on="vid")

# Print the column names of the taxi_own_veh
print(taxi_own_veh.columns)

# Merge the taxi_owners and taxi_veh tables setting a suffix
taxi_own_veh = taxi_owners.merge(taxi_veh, on="vid", suffixes=["_own", "_veh"])

# Print the column names of taxi_own_veh
print(taxi_own_veh.columns)

# Merge the taxi_owners and taxi_veh tables setting a suffix
taxi_own_veh = taxi_owners.merge(taxi_veh, on="vid", suffixes=("_own", "_veh"))

# Print the value_counts to find the most popular fuel_type
print(taxi_own_veh["fuel_type"].value_counts())
