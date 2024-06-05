import xgboost as xgb
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

data = load_diabetes()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Increase the number of trees and maximum depth
n_estimators = 2  # Increase the number of trees
max_depth = 6  # Increase the maximum depth of each tree

xgb_reg = xgb.XGBRegressor(n_estimators=n_estimators, max_depth=max_depth)
xgb_reg.fit(X_train, y_train)


from giza.zkcook import serialize_model
serialize_model(xgb_reg, "xgb_diabetes.json")