import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

fff
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


def lift(a, b):
    # Calcuate the mean of a and b
    a_mean = np.mean(a)
    b_mean = np.mean(b)

    # Calculate the lift using a_mean and b_mean
    lift = (b_mean - a_mean) / a_mean

    return str(round(lift * 100, 2)) + "%"


# Print lift() with control and personalization as inputs
print(lift(control, personalization))


def ab_segmentation(segment):
    # Build a for loop for each segment in marketing
    for subsegment in np.unique(marketing[segment].values):
        print(subsegment)

        # Limit marketing to email and subsegment
        email = marketing[(marketing["marketing_channel"] == "Email") & (marketing[segment] == subsegment)]

        subscribers = email.groupby(["user_id", "variant"])["converted"].max()
        subscribers = pd.DataFrame(subscribers.unstack(level=1))
        control = subscribers["control"].dropna()
        personalization = subscribers["personalization"].dropna()

        # Assuming `df` is the DataFrame containing the data
        control = control.astype(float)
        personalization = personalization.astype(float)

        print("lift:", lift(control, personalization))
        print("t-statistic:", stats.ttest_ind(control, personalization), "\n\n")


# Use ab_segmentation on language displayed
ab_segmentation("language_displayed")

# Use ab_segmentation on age group
ab_segmentation("age_group")
