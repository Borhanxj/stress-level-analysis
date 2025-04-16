import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load merged data
df = pd.read_csv("data/merged_stress_economics.csv")

# Select relevant numeric columns
cols = [
    "High", "Unemployment rate", "CPI", "Life expectancy",
    "Physicians per thousand", "Out of pocket health expenditure", "Tax revenue (%)"
]
corr = df[cols].corr()

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap: High Stress vs Economic Indicators")
plt.tight_layout()
plt.savefig("eda/stress_correlation_heatmap.png")
