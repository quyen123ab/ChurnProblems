# What exactly you want to do ?
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv(r"C:\Users\ADMIN\Downloads\WA_Fn-UseC_-Telco-Customer-Churn.csv") 

df = df.drop(columns=["customerID"])

df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

# Chuyển đổi các cột có dữ liệu dạng phân loại (category)
label_encoders = {}
for col in df.select_dtypes(include=["object"]).columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

X = df.drop(columns=["Churn"])  
y = df["Churn"]  

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

feature_importance_df = pd.DataFrame({
    "Feature": df.drop(columns=["Churn"]).columns,
    "Importance": model.feature_importances_
}).sort_values(by="Importance", ascending=False)

plt.figure(figsize=(12, 8))
sns.barplot(x="Importance", y="Feature", data=feature_importance_df.head(21), palette="viridis")
plt.xlabel("Feature Importance")
plt.ylabel("Feature")
plt.title("Top 21 Most Important Features")
plt.show()
