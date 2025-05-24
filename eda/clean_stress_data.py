import pandas as pd

# Load dataset
df = pd.read_csv("data/Stress_Data.csv")

# Drop irrelevant columns
drop_cols = ["Timestamp", "Mental_Health_Condition"]
df = df.drop(columns=drop_cols, errors="ignore")

# Drop rows with missing target (Stress_Level)
df = df.dropna(subset=["Stress_Level"])

# Drop any other missing values
df_cleaned = df.dropna()

# Save cleaned data
df_cleaned.to_csv("data/cleaned_stress_data_modeling.csv", index=False)
