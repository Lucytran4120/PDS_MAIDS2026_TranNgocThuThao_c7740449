import warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="sklearn")









import matplotlib.pyplot as plt
import pandas as pd
data = {
"Hours_Studied": [1,2,3,4,5,6,7,8,9,10],
"Exam_Score": [40,42,50,55,60,65,70,75,85,90]
}
df = pd.DataFrame(data)
print(df)

# x is Hours_studied, y is Exam_score. X is feature independence, and Y is dependended on x
#plotting visualy
plt.scatter(df["Hours_Studied"], df["Exam_Score"])
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Study Hours vs Exam Score")
plt.show()
# not fully straight because data is variable ( can change abit)

#Prepare training data
X = df[["Hours_Studied"]]
y = df["Exam_Score"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# dataset always be devided into 70-30 ratio or 80-20 ratio, where majority (higher side) is in trainging set

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print(predictions)

from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
print("Mean Squared Error:", mse)
print("R² Score:", r2)

plt.scatter(X, y)
plt.plot(X, model.predict(X), color="red")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.show()

model.predict([[7.5]])



