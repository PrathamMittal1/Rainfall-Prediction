import pickle
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
# from sklearn.metrics import r2_score, mean_squared_error
# from sklearn.model_selection import train_test_split

data = pd.read_csv("precipitation_NASA_data.csv")  # loading training dataset
x = data.iloc[0:, 3:9].values
y = data.iloc[0:, 9].values
regressor = GradientBoostingRegressor()  # building regression model
regressor.fit(x, y)
with open("trained_model.pkl", 'wb') as fl:
    pickle.dump(regressor, fl)                # saving trained model
    print('Model trained and Saved')
