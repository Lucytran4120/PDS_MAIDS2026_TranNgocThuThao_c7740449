import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
import pickle
# df= pd.read_csv('data/AirQualityUCI.csv')
df = pd.read_excel('data/AirQualityUCI.xlsx')
print(df.head())


X = df.iloc[:, 2:14]  # Columns 2 through 13 (12 features)
Y = df.iloc[:, 14]    # Column 14 (the 15th and last column)

test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y,test_size=test_size, random_state=seed)
# Fit the model on training set

model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, Y_train)

# save the model to disk
filename = 'RF_ AIRQUALITY.sav'
pickle.dump(model, open(filename, 'wb'))
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, Y_test)
print(result)