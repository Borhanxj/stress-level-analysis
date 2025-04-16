import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load merged dataset
df = pd.read_csv("data/merged_stress_economics.csv")

# Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x="Out of pocket health expenditure",
    y="Life expectancy",
    size="High",
    hue="High",
    palette="coolwarm",
    sizes=(100, 800),
    legend="brief"
)

plt.title("Out-of-Pocket Health Spending vs Life Expectancy\n(Sized by High Stress %)")
plt.xlabel("Out-of-Pocket Health Expenditure (%)")
plt.ylabel("Life Expectancy (Years)")
plt.legend(title="High Stress %", loc="lower left")
plt.grid(True)
plt.tight_layout()
plt.savefig("eda/health_vs_life_stress.png")
