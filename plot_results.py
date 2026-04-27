import pandas as pd
import matplotlib.pyplot as plt

# ======================
# Load forecast output
# ======================
df = pd.read_excel("forecast_output.xlsx")

# Convert date
df['ds'] = pd.to_datetime(df['ds'])

# ======================
# Plot forecast
# ======================
plt.figure()

# Actual prediction line
plt.plot(df['ds'], df['yhat'], label='Prediction')

# Confidence interval
plt.fill_between(df['ds'], df['yhat_lower'], df['yhat_upper'], alpha=0.3)

# Labels
plt.xlabel("Date")
plt.ylabel("Amount")
plt.title("Expense Forecast")

plt.legend()

# Show plot
plt.show()