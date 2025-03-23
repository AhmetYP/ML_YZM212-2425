import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns


def sigmoid(z):
    return 1 / (1 + np.exp(-z))



def compute_cost(y, y_pred):
    m = len(y)
    return - (1 / m) * np.sum(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))



def gradient_descent(X, y, lr=0.01, epochs=1000):
    m, n = X.shape
    weights = np.zeros(n)
    bias = 0
    cost_history = []

    for i in range(epochs):
        linear_model = np.dot(X, weights) + bias
        y_pred = sigmoid(linear_model)


        dw = (1 / m) * np.dot(X.T, (y_pred - y))
        db = (1 / m) * np.sum(y_pred - y)

        weights -= lr * dw
        bias -= lr * db


        cost = compute_cost(y, y_pred)
        cost_history.append(cost)

    return weights, bias, cost_history



def predict(X, weights, bias):
    linear_model = np.dot(X, weights) + bias
    y_pred = sigmoid(linear_model)
    return [1 if i > 0.5 else 0 for i in y_pred]


# Veri setini yükleyelim
file_path = "cleaned_loan_data.csv"
df = pd.read_csv(file_path)


X = df.drop(columns=["loan_status"]).values
y = df["loan_status"].values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


start_time = time.time()
weights, bias, cost_history = gradient_descent(X_train, y_train, lr=0.01, epochs=1000)
train_time = time.time() - start_time


start_time = time.time()
y_pred = predict(X_test, weights, bias)
test_time = time.time() - start_time


accuracy = accuracy_score(y_test, y_pred)


conf_matrix = confusion_matrix(y_test, y_pred)


print(f"Model Accuracy: {accuracy:.4f}")
print(f"Training Time: {train_time:.4f} seconds")
print(f"Testing Time: {test_time:.4f} seconds")
print("\nClassification Report:\n", classification_report(y_test, y_pred))


plt.plot(range(len(cost_history)), cost_history)
plt.xlabel("Epochs")
plt.ylabel("Cost")
plt.title("Cost Function Over Epochs")
plt.show()


plt.figure(figsize=(6, 4))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=["Rejected", "Approved"],
            yticklabels=["Rejected", "Approved"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()
