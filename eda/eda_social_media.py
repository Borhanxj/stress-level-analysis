import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/social_media_stress.csv")

# Clean age
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df.dropna(subset=["Age"], inplace=True)

# Plot: Daily Usage Time by Emotion
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Dominant_Emotion', y='Daily_Usage_Time (minutes)')
plt.title('Daily Usage Time by Emotion')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("eda/boxplot_usage_emotion.png")
