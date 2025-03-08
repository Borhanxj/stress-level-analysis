import pdfplumber
import pandas as pd

# Define PDF file paths (these should match your GitHub repo structure)
oecd_pdf_path = "data/OECD_Income_Data.pdf"
gallup_pdf_path = "data/Gallup_Stress_Report_2024.pdf"

# Function to extract tables from PDF and convert to CSV
def extract_tables_from_pdf(pdf_path, output_csv_path):
    extracted_tables = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                df = pd.DataFrame(table)
                extracted_tables.append(df)
    
    # Combine all extracted tables into a single dataframe
    if extracted_tables:
        combined_df = pd.concat(extracted_tables, ignore_index=True)
        combined_df.to_csv(output_csv_path, index=False)
        print(f"✅ Extracted tables saved to {output_csv_path}")
    else:
        print(f"⚠️ No tables found in {pdf_path}")

# Extract data from PDFs
extract_tables_from_pdf(oecd_pdf_path, "data/OECD_Income_Data.csv")
extract_tables_from_pdf(gallup_pdf_path, "data/Gallup_Stress_Report_2024.csv")
