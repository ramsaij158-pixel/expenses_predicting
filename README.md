# Expenses Predicting

A beginner-to-intermediate machine-learning project for forecasting student expenses using Excel data, Pandas and Prophet.

## Project Goal

This project analyses student spending data and predicts future expenses. It is an early version of my student finance forecasting work.

## What This Project Does

- Combines expense data from Excel files
- Groups spending by date and category
- Creates holiday/event data for forecasting
- Builds a Prophet model for 30-day expense prediction
- Saves forecast results into Excel
- Plots forecast values with confidence intervals

## Main Files

| File | Purpose |
|---|---|
| `category.py` | Combines Excel data and creates daily/category grouped files |
| ` split_data.py` | Splits expense data into category files and prepares holiday data |
| `prophet_model.py` | Trains Prophet and creates a 30-day forecast |
| `plot_results.py` | Visualizes forecast output |
| `student_data.xlsx` | Input student expense data |
| `daily_total.xlsx` | Daily total spending used for forecasting |
| `forecast_output.xlsx` | Forecasted values from the Prophet model |

## Tech Stack

- Python
- Pandas
- Prophet
- Matplotlib
- Excel

## How to Run

Install required packages:

```bash
pip install pandas prophet matplotlib openpyxl
```

Run the data-preparation step:

```bash
python category.py
```

Run the forecast:

```bash
python prophet_model.py
```

Plot the results:

```bash
python plot_results.py
```

## Learning Outcomes

- Learned how to prepare Excel data for machine learning
- Practiced time-series forecasting using Prophet
- Created daily and category-wise summaries
- Exported model results back into Excel
- Built the foundation for a more advanced finance dashboard

## Future Improvements

- Rename files consistently
- Add screenshots of forecast charts
- Add model accuracy metrics
- Build a Streamlit dashboard
- Move repeated logic into reusable functions

