import pandas as pd
import os

# Load both Excel files
file1 = pd.read_excel("student_data.xlsx")
file2 = pd.read_excel("excel_excel_xlsx.xlsx")

# Combine them
df = pd.concat([file1, file2], ignore_index=True)

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# ======================
# Extract holidays
# ======================
events_df = df[df['Event'].notna()][['Date', 'Event']]
events_df = events_df.rename(columns={'Date': 'ds', 'Event': 'holiday'})
events_df = events_df.drop_duplicates()

events_df.to_excel("holidays.xlsx", index=False)

# ======================
# Remove event column
# ======================
df_clean = df.drop(columns=['Event'])

# ======================
# Create folder
# ======================
os.makedirs("category_files", exist_ok=True)

# ======================
# Split categories
# ======================
grouped = df_clean.groupby("Category")

for category, data in grouped:
    data = data.sort_values("Date")
    data.to_excel(f"category_files/{category}.xlsx", index=False)

print("✅ Done! Files created")