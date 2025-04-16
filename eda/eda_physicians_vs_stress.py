import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load merged data
df = pd.read_csv("data/merged_stress_economics.csv")

# Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x="Physicians per thousand",
    y="High",
    size="Population",
    hue="Country",
    sizes=(100, 800),
    palette="deep",
    legend="brief"
)

plt.title("Physician Density vs High Stress Proportion")
plt.xlabel("Physicians per 1,000 People")
plt.ylabel("Proportion of Population Reporting High Stress")
plt.grid(True)
plt.tight_layout()
plt.savefig("eda/physicians_vs_stress.png")
