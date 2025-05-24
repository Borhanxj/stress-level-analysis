
import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("StressLevelDataset.csv")

# Separate features and target
X = df.drop(columns=["stress_level"])
y = df["stress_level"]

# Split into train and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Save to CSV
X_train.to_csv("X_train_final.csv", index=False)
X_test.to_csv("X_test_final.csv", index=False)
y_train.to_csv("y_train_final.csv", index=False)
y_test.to_csv("y_test_final.csv", index=False)

print("Data successfully split and saved.")
