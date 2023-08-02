import pandas as pd

taxi_owners = pd.read_csv("taxi_owners.csv", index_col=0, header=0)
taxi_veh = pd.read_csv("taxi_veh.csv", index_col=0, header=0)

# Merge the taxi_owners and taxi_veh tables
taxi_own_veh = taxi_owners.merge(taxi_veh, on="vid")

# Print the column names of the taxi_own_veh
print(taxi_own_veh.columns)
