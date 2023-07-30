import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marketing = pd.read_csv("marketing.csv", parse_dates=["date_served", "date_subscribed", "date_canceled"])


def conversion_rate(dataframe, column_names):
    # Total number of converted users
    column_conv = dataframe[dataframe["converted"] == True].groupby(column_names)["user_id"].nunique()

    # Total number users
    column_total = dataframe.groupby(column_names)["user_id"].nunique()

    # Conversion rate
    conversion_rate = column_conv / column_total

    # Fill missing values with 0
    conversion_rate = conversion_rate.fillna(0)
    return conversion_rate


# Calculate conversion rate by age_group
age_group_conv = conversion_rate(marketing, ["date_served", "age_group"])
print(age_group_conv)

# Unstack and create a DataFrame
age_group_df = pd.DataFrame(age_group_conv.unstack(level=1))

# Visualize conversion by age_group
age_group_df.plot()
plt.title("Conversion rate by age group\n", size=16)
plt.ylabel("Conversion rate", size=14)
plt.xlabel("Age group", size=14)
plt.show()


def plotting_conv(dataframe):
    for column in dataframe:
        # Plot column by dataframe's index
        plt.plot(dataframe.index, dataframe[column])
        plt.title("Daily " + str(column) + " conversion rate\n", size=16)
        plt.ylabel("Conversion rate", size=14)
        plt.xlabel("Date", size=14)
        # Show plot
        plt.show()
        plt.clf()


# Calculate conversion rate by date served and age group
age_group_conv = conversion_rate(marketing, ["date_served", "age_group"])

# Unstack age_group_conv and create a DataFrame
age_group_df = pd.DataFrame(age_group_conv.unstack(level=1))

# Plot the results
plotting_conv(age_group_df)

# Calculate conversion rate by date served and channel
daily_conv_channel = conversion_rate(marketing, ["date_served", "marketing_channel"])

print(daily_conv_channel.head())

# Unstack daily_conv_channel and convert it to a DataFrame
daily_conv_channel = pd.DataFrame(daily_conv_channel.unstack(level=1))

# Plot results of daily_conv_channel
plotting_conv(daily_conv_channel)

# Add day of week column to marketing
marketing["DoW_served"] = marketing["date_served"].dt.dayofweek

# Calculate conversion rate by day of week
DoW_conversion = conversion_rate(marketing, ["DoW_served", "marketing_channel"])

# Unstack channels
DoW_df = pd.DataFrame(DoW_conversion.unstack(level=1))

# Plot conversion rate by day of week
DoW_df.plot()
plt.title("Conversion rate by day of week\n")
plt.ylim(0)
plt.show()

# Isolate the rows where marketing channel is House Ads
house_ads = marketing[marketing["marketing_channel"] == "House Ads"]

# Calculate conversion by date served, and language displayed
conv_lang_channel = conversion_rate(house_ads, ["date_served", "language_displayed"])

# Unstack conv_lang_channel
conv_lang_df = pd.DataFrame(conv_lang_channel.unstack(level=1))

# Use your plotting function to display results
plotting_conv(conv_lang_df)

# Add the new column is_correct_lang
house_ads["is_correct_lang"] = np.where(house_ads["language_displayed"] == house_ads["language_preferred"], "Yes", "No")

# Groupby date_served and correct_language
language_check = house_ads.groupby(["date_served", "is_correct_lang"])["user_id"].count()

# Unstack language_check and fill missing values with 0's
language_check_df = pd.DataFrame(language_check.unstack(level=1)).fillna(0)

# Print results
print(language_check_df)
