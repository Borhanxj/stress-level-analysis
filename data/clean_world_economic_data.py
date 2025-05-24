
import pandas as pd

# Load dataset
df = pd.read_csv('World_Economic_Data.csv')

# List of columns to clean
columns_to_clean = [
    'Unemployment rate',
    'CPI',
    'Life expectancy',
    'Tax revenue (%)',
    'Population: Labor force participation (%)'
]

# Clean columns: remove % and commas, convert to numeric
for col in columns_to_clean:
    if col in df.columns:
        df[col] = df[col].astype(str).str.replace('%', '', regex=False)
        df[col] = df[col].str.replace(',', '', regex=False)
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Save cleaned data
df.to_csv('cleaned_World_Economic_Data.csv', index=False)
