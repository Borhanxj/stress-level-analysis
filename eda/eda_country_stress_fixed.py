import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/Stress_Data.csv")

# Filter top 10 countries with highest count of "High" stress
top_countries = (
    df[df["Stress_Level"] == "High"]
    .groupby("Country")
    .size()
    .sort_values(ascending=False)
    .head(10)
    .index
)

filtered_df = df[df["Country"].isin(top_countries)]

# Plot: Stress Level Distribution in Top Countries
plt.figure(figsize=(12, 6))
sns.countplot(data=filtered_df, x="Country", hue="Stress_Level", palette="muted")
plt.title("Stress Level Distribution in Top 10 High-Stress Countries")
plt.xticks(rotation=30)
plt.ylabel("Number of People")
plt.tight_layout()
plt.savefig("eda/country_stress_distribution.png")
