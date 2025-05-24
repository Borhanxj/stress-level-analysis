
import pandas as pd
from sklearn.model_selection import train_test_split

# Load cleaned and ML-ready dataset
df = pd.read_csv('ml_ready_Stress_Data.csv')

# Split into features (X) and target (y)
X = df.drop(columns=['Stress_Level'])
y = df['Stress_Level']

# 80/20 train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save splits to CSV
X_train.to_csv('X_train.csv', index=False)
X_test.to_csv('X_test.csv', index=False)
y_train.to_csv('y_train.csv', index=False)
y_test.to_csv('y_test.csv', index=False)
