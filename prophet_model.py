import pandas as pd
from prophet import Prophet

# ======================
# Load data
# ======================
df = pd.read_excel("daily_total.xlsx")

# Convert to Prophet format
df = df.rename(columns={
    "Date": "ds",
    "Amount": "y"
})

df['ds'] = pd.to_datetime(df['ds'])

# ======================
# Load holidays (optional but recommended)
# ======================
holidays = pd.read_excel("holidays.xlsx")

# ======================
# Create model
# ======================
model = Prophet(holidays=holidays)

# Train model
model.fit(df)

# ======================
# Create future dates
# ======================
future = model.make_future_dataframe(periods=30)

# Predict
forecast = model.predict(future)

# ======================
# Save output
# ======================
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_excel(
    "forecast_output.xlsx", index=False
)

print("✅ Forecast completed and saved")