
import pandas as pd

# Load dataset
df = pd.read_csv('Stress_Data.csv')

# Convert Age to numeric and filter out unrealistic values
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df = df[(df['Age'].notnull()) & (df['Age'] >= 13) & (df['Age'] <= 100)]

# Drop rows with missing values in critical columns
critical_columns = [
    'Age', 'Gender', 'Mental_Health_Condition',
    'Stress_Level', 'Sleep_Hours', 'Work_Hours', 'Physical_Activity_Hours'
]
df = df.dropna(subset=critical_columns)

# Standardize categorical text columns
for col in ['Gender', 'Mental_Health_Condition', 'Stress_Level']:
    df[col] = df[col].str.strip().str.title()

# Save cleaned dataset
df.to_csv('cleaned_Stress_Data.csv', index=False)
