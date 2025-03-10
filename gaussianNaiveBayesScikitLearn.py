import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

# Veri setinin yüklenmesi
data1 = pd.read_csv("C:/Users/ahmet/PycharmProjects/PythonProject3/data.csv")

print(data1.head())
print(data1.shape)
print(data1.dtypes)

print(data1.info)

# Gereksiz sütunların çıkarılması
data1.drop(['Unnamed: 32', 'id'], axis=1, inplace=True)

# Etiketleme (Label Encoding)
labelencoder = LabelEncoder()
data1['diagnosis'] = labelencoder.fit_transform(data1['diagnosis'])

# Özellikler ve hedef değişkenin ayrılması (NumPy'ye dönüştürülüyor)
y = data1['diagnosis'].to_numpy()
X = data1.drop('diagnosis', axis=1).to_numpy()

print(type(X), type(y))

# Eğitim ve test setlerine bölme
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Gaussian Naive Bayes modelini oluşturma
classifier = GaussianNB()

# Modelin eğitimi ve zamanı ölçme
start_train = time.time()
classifier.fit(X_train, y_train)
end_train = time.time()

# Modelin tahmini ve zamanı ölçme
start_predict = time.time()
y_pred = classifier.predict(X_test)
end_predict = time.time()

# Performans metrikleri
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

# Eğitim ve tahmin süreleri
training_time = end_train - start_train
prediction_time = end_predict - start_predict

# Karmaşıklık matrisini NumPy ile normalize etme
conf_matrix_normalized = conf_matrix / conf_matrix.sum(axis=1, keepdims=True)

# Karmaşıklık matrisini görselleştirme (matplotlib ile)
plt.figure(figsize=(8, 6))
plt.imshow(conf_matrix_normalized, interpolation='nearest', cmap=plt.cm.Blues)
plt.title("Confusion Matrix (Normalized) - Gaussian Naive Bayes")
plt.colorbar()

# Etiketler ekleme
classes = ['Benign (0)', 'Malignant (1)']
tick_marks = np.arange(len(classes))
plt.xticks(tick_marks, classes, rotation=45)
plt.yticks(tick_marks, classes)

# Normalized matris değerlerini görselleştirme
thresh = conf_matrix_normalized.max() / 2.0
for i, j in np.ndindex(conf_matrix_normalized.shape):
    plt.text(j, i, f"{conf_matrix[i, j]} ({conf_matrix_normalized[i, j]:.2f})",
             horizontalalignment="center",
             color="white" if conf_matrix_normalized[i, j] > thresh else "black")

plt.ylabel('True Label')
plt.xlabel('Predicted Label')
plt.tight_layout()
plt.show()

# Sonuçları yazdırma
print(f"Eğitim Süresi: {training_time:.4f} saniye")
print(f"Tahmin Süresi: {prediction_time:.4f} saniye")
print(f"Doğruluk (Accuracy): {accuracy:.2%}")
