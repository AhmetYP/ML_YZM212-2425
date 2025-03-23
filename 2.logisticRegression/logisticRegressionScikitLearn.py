import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns


file_path = "C:/Users/ahmet/PycharmProjects/PythonProject4/cleaned_loan_data.csv"
df = pd.read_csv(file_path)


X = df.drop(columns=["loan_status"])
y = df["loan_status"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


start_time = time.time()
model = LogisticRegression()
model.fit(X_train, y_train)
train_time = time.time() - start_time


start_time = time.time()
y_pred = model.predict(X_test)
test_time = time.time() - start_time


accuracy = accuracy_score(y_test, y_pred)


conf_matrix = confusion_matrix(y_test, y_pred)


print(f"Model Accuracy: {accuracy:.4f}")
print(f"Training Time: {train_time:.4f} seconds")
print(f"Testing Time: {test_time:.4f} seconds")
print("\nClassification Report:\n", classification_report(y_test, y_pred))


plt.figure(figsize=(6,4))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=["Rejected", "Approved"], yticklabels=["Rejected", "Approved"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()
