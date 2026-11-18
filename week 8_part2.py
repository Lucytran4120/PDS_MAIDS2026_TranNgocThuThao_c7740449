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