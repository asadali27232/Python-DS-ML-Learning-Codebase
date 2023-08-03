import pickle as pkl
import pandas as pd

with open("ward.p", "rb") as f:
    object = pkl.load(f)

df = pd.DataFrame(object)
df.to_csv(r"wards.csv")

with open("census.p", "rb") as f:
    object = pkl.load(f)

df = pd.DataFrame(object)
df.to_csv(r"census.csv")
