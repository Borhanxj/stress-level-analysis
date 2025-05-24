
import pandas as pd

# Load cleaned stress data
df = pd.read_csv('cleaned_Stress_Data.csv')

# Drop irrelevant columns
df.drop(columns=['User_ID', 'Severity'], inplace=True, errors='ignore')

# Remove rows with 'Prefer not to say' in Gender
df = df[df['Gender'].str.lower() != 'prefer not to say']

# Convert Stress_Level to binary label
# High = 1, Not High = 0
df['Stress_Level'] = df['Stress_Level'].apply(lambda x: 1 if x.lower() == 'high' else 0)

# Save cleaned file ready for ML modeling
df.to_csv('ml_ready_Stress_Data.csv', index=False)
