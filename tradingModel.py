import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error, r2_score, explained_variance_score, mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
stock = pd.read_csv("NIFTY_EOD.csv")

data = stock


# Split the data into features and target
y = data['close_forecast']
X = data.drop(columns=['Ticker','Date/Time','close_forecast'], axis=1)


# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train an XGBoost model
model = xgb.XGBRegressor(objective='reg:squarederror', random_state=42, booster='gbtree')
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Add predicted prices to test data
predicted_prices = X_test.copy()
predicted_prices['Close'] = y_pred



# Calculate evaluation metrics
mape = mean_absolute_percentage_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
explained_var = explained_variance_score(y_test, y_pred)



# Print the evaluation metrics and directional accuracy
print("MAPE:", mape)
print("Mean squared error:", mse)
print("Root mean squared error:", rmse)
print("Mean absolute error:", mae)
print("R-squared:", r2)
print("Explained variance:", explained_var)





# Predict the next day close and direction
next_day = X.tail(1)
next_day_pred = model.predict(next_day)
next_day_close = next_day_pred[0]
print("Next day predicted close:", next_day_close)




# Store the predicted vs actual values and direction in a separate csv
predictions = pd.DataFrame({'Date/Time': X_test.index, 'Actual': y_test.values, 'Predicted': y_pred})
predictions.to_csv("NIFTY_xgboost_predictions.csv", index=False)

# Plot feature importance using Matplotlib
fig, ax = plt.subplots(figsize=(10, 8))
xgb.plot_importance(model, ax=ax, importance_type='gain')
plt.title('Feature Importance')
plt.show()
