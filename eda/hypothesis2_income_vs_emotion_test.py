import pandas as pd
from scipy.stats import ttest_ind

# Load datasets
gallup = pd.read_csv("data/cleaned_gallup_emotion_data.csv")
oecd = pd.read_csv("data/cleaned_oecd_income_data.csv")

# Merge datasets on Country
merged = pd.merge(gallup, oecd, on="Country", how="inner")

# Split by median income
threshold = merged["Disposable_Income_USD"].median()
low_income = merged[merged["Disposable_Income_USD"] < threshold]
high_income = merged[merged["Disposable_Income_USD"] >= threshold]

# Run t-test
result = ttest_ind(low_income["Positive_Experience_Index"], high_income["Positive_Experience_Index"])

# Print results
print("Positive Experience Index (Low vs High Income):")
print("t =", round(result.statistic, 4), ", p =", round(result.pvalue, 4))
