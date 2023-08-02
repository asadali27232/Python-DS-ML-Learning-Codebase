import pickle as pkl
import pandas as pd

with open("taxi_owners.p", "rb") as f:
    object = pkl.load(f)

df = pd.DataFrame(object)
df.to_csv(r"taxi_owners.csv")
