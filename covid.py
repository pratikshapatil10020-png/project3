import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("covid_data.csv")

print("Dataset Loaded Successfully!\n")

# Display first 5 rows
print(df.head())

# -----------------------------
# Data Cleaning
# -----------------------------
df.fillna(0, inplace=True)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# -----------------------------
# Overall Statistics
# -----------------------------
print("\n===== COVID-19 Statistics =====")

print("Total Confirmed Cases :", df["Confirmed"].sum())
print("Total Death Cases     :", df["Deaths"].sum())
print("Total Recovered Cases :", df["Recovered"].sum())

# -----------------------------
# Calculate Active Cases
# -----------------------------
df["Active"] = (
    df["Confirmed"] -
    df["Deaths"] -
    df["Recovered"]
)

# -----------------------------
# Top 10 Countries
# -----------------------------
top_countries = (
    df.groupby("Country")
    ["Confirmed"]
    .max()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Affected Countries")
print(top_countries)

# -----------------------------
# Plot 1
# Top Countries
# -----------------------------
plt.figure(figsize=(10,6))

top_countries.plot(kind='bar', color='skyblue')

plt.title("Top 10 Countries by Confirmed Cases")
plt.xlabel("Country")
plt.ylabel("Confirmed Cases")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# -----------------------------
# Plot 2
# Global Cases Over Time
# -----------------------------
daily_cases = (
    df.groupby("Date")
    ["Confirmed"]
    .sum()
)

plt.figure(figsize=(12,6))

plt.plot(
    daily_cases.index,
    daily_cases.values,
    color='red',
    linewidth=2
)

plt.title("Global Confirmed Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")

plt.grid(True)

plt.show()

# -----------------------------
# Plot 3
# Pie Chart
# -----------------------------
latest = df.iloc[-1]

sizes = [
    latest["Recovered"],
    latest["Deaths"],
    latest["Active"]
]

labels = [
    "Recovered",
    "Deaths",
    "Active"
]

plt.figure(figsize=(6,6))

plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("COVID-19 Case Distribution")

plt.show()

# -----------------------------
# Plot 4
# Correlation Heatmap
# -----------------------------
plt.figure(figsize=(8,6))

sns.heatmap(
    df[
        [
            "Confirmed",
            "Recovered",
            "Deaths",
            "Active"
        ]
    ].corr(),
    annot=True,
    cmap="Blues"
)

plt.title("Correlation Heatmap")

plt.show()

# -----------------------------
# Plot 5
# Daily New Cases
# -----------------------------
df["New Cases"] = df["Confirmed"].diff()

plt.figure(figsize=(12,6))

plt.plot(
    df["Date"],
    df["New Cases"],
    color="green"
)

plt.title("Daily New COVID-19 Cases")

plt.xlabel("Date")
plt.ylabel("New Cases")

plt.grid(True)

plt.show()

print("\nAnalysis Completed Successfully!")


OUTPUT:
Dataset Loaded Successfully!

===== COVID-19 Statistics =====

Total Confirmed Cases : 10790
Total Death Cases     : 372
Total Recovered Cases : 7235

Top 10 Affected Countries

USA    3200

Analysis Completed Successfully!

It will also generate: