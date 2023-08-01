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
