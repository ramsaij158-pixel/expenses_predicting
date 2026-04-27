import pandas as pd

# ======================
# Load files
# ======================
df1 = pd.read_excel("student_data.xlsx")
df2 = pd.read_excel("excel_excel_xlsx.xlsx")

# Combine
df = pd.concat([df1, df2], ignore_index=True)

# Convert date
df['Date'] = pd.to_datetime(df['Date'])

# ======================
# 1. Total per day (IMPORTANT for Prophet)
# ======================
daily_total = df.groupby('Date')['Amount'].sum().reset_index()

# Save
daily_total.to_excel("daily_total.xlsx", index=False)

print("✅ Daily total file created")

# ======================
# 2. Category-wise grouped (optional)
# ======================
category_group = df.groupby(['Date', 'Category'])['Amount'].sum().reset_index()

# Save
category_group.to_excel("category_grouped.xlsx", index=False)

print("✅ Category grouped file created")