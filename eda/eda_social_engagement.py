import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/social_media_stress.csv")

# Clean age column
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df.dropna(subset=["Age"], inplace=True)

# Plot: Likes, Comments, and Messages vs Emotion
fig, axs = plt.subplots(1, 3, figsize=(20, 6))

sns.violinplot(data=df, x="Dominant_Emotion", y="Likes_Received_Per_Day", ax=axs[0], palette="muted")
axs[0].set_title("Likes per Day by Emotion")
axs[0].tick_params(axis='x', rotation=30)

sns.violinplot(data=df, x="Dominant_Emotion", y="Comments_Received_Per_Day", ax=axs[1], palette="pastel")
axs[1].set_title("Comments per Day by Emotion")
axs[1].tick_params(axis='x', rotation=30)

sns.violinplot(data=df, x="Dominant_Emotion", y="Messages_Sent_Per_Day", ax=axs[2], palette="Set2")
axs[2].set_title("Messages Sent per Day by Emotion")
axs[2].tick_params(axis='x', rotation=30)

plt.tight_layout()
plt.savefig("eda/violin_engagement_emotion.png")
