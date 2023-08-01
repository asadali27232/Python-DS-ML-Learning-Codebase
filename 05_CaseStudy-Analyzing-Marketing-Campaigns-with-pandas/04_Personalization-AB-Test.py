import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marketing = pd.read_csv("marketing.csv", parse_dates=["date_served", "date_subscribed", "date_canceled"])

# Subset the DataFrame
email = marketing[marketing["marketing_channel"] == "Email"]

# Group the email DataFrame by variant
alloc = email.groupby("variant")["user_id"].nunique()

# Plot a bar chart of the test allocation
alloc.plot(kind="bar")
plt.title("Personalization test allocation")
plt.ylabel("# participants")
plt.show()

print(email.tail(20))

subscribers = email.groupby(["user_id", "variant"]).max()
print(subscribers.head())
subscribers_df = pd.DataFrame(subscribers.unstack(level=1))
print(subscribers_df.head())

# Group marketing by user_id and variant
subscribers = email.groupby(["user_id", "variant"])["converted"].max()
subscribers_df = pd.DataFrame(subscribers.unstack(level=1))

# Drop missing values from the control column
control = subscribers_df["control"].dropna()

# Drop missing values from the personalization column
personalization = subscribers_df["personalization"].dropna()

print("Control conversion rate:", control.value_counts().get(True, 0) / control.count())
print("Personalization conversion rate:", personalization.value_counts().get(True, 0) / personalization.count())






