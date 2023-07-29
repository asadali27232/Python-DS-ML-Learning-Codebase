# In this chapter, you will learn about common marketing metrics and how to calculate them using pandas. You will also visualize your results and practice user segmentation.
import pandas as pd
import matplotlib.pyplot as plt

marketing = pd.read_csv("marketing.csv", parse_dates=["date_served", "date_subscribed", "date_canceled"])

# Calculate the number of people we marketed to
total = marketing["user_id"].nunique()

# Calculate the number of people who subscribed
subscribers = marketing[marketing["converted"] == True]["user_id"].nunique()

# Calculate the conversion rate
conversion_rate = subscribers / total
print(round(conversion_rate * 100, 2), "%")

# Calculate the number of subscribers
total_subscribers = marketing[marketing["converted"] == True]["user_id"].nunique()

# Calculate the number of people who remained subscribed
retained = marketing[marketing["is_retained"] == True]["user_id"].nunique()

# Calculate the retention rate
retention_rate = retained / total_subscribers
print(round(retention_rate * 100, 2), "%")

# Isolate english speakers
english_speakers = marketing[marketing["language_displayed"] == "English"]

# Calculate the total number of English speaking users
total = english_speakers["user_id"].nunique()

# Calculate the number of English speakers who converted
subscribers = english_speakers[english_speakers["converted"] == True]["user_id"].nunique()

# Calculate conversion rate
conversion_rate = subscribers / total
print("English speaker conversion rate:", round(conversion_rate * 100, 2), "%")

# Group by language_displayed and count unique users
total = marketing.groupby("language_displayed")["user_id"].nunique()

# Group by language_displayed and count unique conversions
subscribers = marketing[marketing["converted"] == True].groupby("language_displayed")["user_id"].nunique()

# Calculate the conversion rate for all languages
language_conversion_rate = subscribers / total
print(language_conversion_rate)

# Group by date_served and count unique users
total = marketing.groupby("date_served")["user_id"].nunique()

# Group by date_served and count unique converted users
subscribers = marketing[marketing["converted"] == True].groupby("date_served")["user_id"].nunique()

# Calculate the conversion rate per day
daily_conversion_rate = subscribers / total
print(daily_conversion_rate)

# Create a bar chart using language_conversion_rate DataFrame
language_conversion_rate.plot()

# Add a title and x and y-axis labels
plt.title("Conversion rate by language\n", size=16)
plt.xlabel("Language", size=14)
plt.ylabel("Conversion rate (%)", size=14)

# Display the plot
plt.show()

# Group by date_served and count unique users
total = marketing.groupby(["date_served"])["user_id"].nunique()

# Group by date_served and calculate subscribers
subscribers = marketing[marketing["converted"] == True].groupby(["date_served"])["user_id"].nunique()

# Calculate the conversion rate for all languages
daily_conversion_rates = subscribers / total

# Reset index to turn the results into a DataFrame
daily_conversion_rate = pd.DataFrame(daily_conversion_rates.reset_index(0))

# Rename columns
daily_conversion_rate.columns = ["date_served", "conversion_rate"]

# Create a line chart using daily_conversion_rate DataFrame
daily_conversion_rate.plot("date_served", "conversion_rate")

plt.title("Daily conversion rate\n", size=16)
plt.ylabel("Conversion rate (%)", size=14)
plt.xlabel("Date", size=14)

# Set the y-axis to begin at 0
plt.ylim(0)

# Display the plots
plt.show()

channel_age = marketing.groupby(["marketing_channel", "age_group"])["user_id"].count()

# Unstack channel_age and transform it into a DataFrame
channel_age_df = pd.DataFrame(channel_age.unstack(level=1))

# Plot channel_age
channel_age_df.plot(kind="bar")
plt.title("Marketing channels by age group")
plt.xlabel("Age Group")
plt.ylabel("Users")

# Add a legend to the plot
plt.legend(loc="upper right", labels=channel_age_df.columns.values)
plt.show()

# Count the subs by subscribing channel and day
retention_total = marketing.groupby(["date_subscribed", "subscribing_channel"])["user_id"].nunique()

# Print results
print(retention_total.head())

# Sum the retained subs by subscribing channel and date subscribed
retention_subs = marketing[marketing['is_retained'] == True].groupby(['date_subscribed', 'subscribing_channel'])['user_id'].nunique()

# Print results
print(retention_subs.head())