import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Load your CSV
# Replace this path with the correct path to your file
file_path = file_path = "C:/Projects/smart-store-ddstcyr/data/prepared/sales_data_prepared.csv"
df = pd.read_csv(file_path)

# 2. Clean column names and values
df.columns = df.columns.str.strip()  # Remove any extra spaces in column names
df['SaleAmount'] = df['SaleAmount'].replace(r'[\$,]', '', regex=True).astype(float)
df['SaleDate'] = pd.to_datetime(df['SaleDate'])

# 3. Aggregate monthly sales
monthly_sales = df.resample('M', on='SaleDate').sum(numeric_only=True).reset_index()[['SaleDate', 'SaleAmount']]
monthly_sales['MonthIndex'] = np.arange(len(monthly_sales))  # Create numeric index for time

# 4. Fit a linear regression model
X = monthly_sales[['MonthIndex']]
y = monthly_sales['SaleAmount']

model = LinearRegression()
model.fit(X, y)

# 5. Forecast the next 6 months
future_index = np.arange(len(monthly_sales), len(monthly_sales) + 6).reshape(-1, 1)
future_sales = model.predict(future_index)

# 6. Create future dates
forecast_months = pd.date_range(start=monthly_sales['SaleDate'].iloc[-1] + pd.offsets.MonthBegin(),
                                periods=6, freq='MS')
forecast_df = pd.DataFrame({
    'SaleDate': forecast_months,
    'SaleAmount': future_sales
})

# 7. Plot the results
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales['SaleDate'], monthly_sales['SaleAmount'], label='Actual Sales')
plt.plot(forecast_df['SaleDate'], forecast_df['SaleAmount'], label='Forecasted Sales', linestyle='--')
plt.title('Sales Forecast (Linear Regression)')
plt.xlabel('Date')
plt.ylabel('Sales Amount')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


Figure_1.png