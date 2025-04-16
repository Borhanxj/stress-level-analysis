import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Gallup data
df = pd.read_csv("data/gallup_emotion_data_2023.csv")

# Plot emotion metric heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.set_index("Country")[["Stress_%", "Worry_%", "Anger_%", "Sadness_%", "Loneliness_%"]],
            cmap="YlOrBr", annot=True, fmt=".0f")
plt.title("Emotion Metrics by Country")
plt.tight_layout()
plt.savefig("eda/emotion_heatmap_table.png")
