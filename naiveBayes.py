import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time


# Gaussian Naive Bayes Sınıfı
class GaussianNaiveBayes:
    def __init__(self):
        self.classes = None
        self.mean = {}
        self.variance = {}
        self.priors = {}
        self.epsilon = 1e-9  # Varyansı sıfır olanlar için küçük bir sabit

    def fit(self, X, y):
        self.classes = np.unique(y)  # Sınıfları belirle
        for cls in self.classes:
            X_cls = X[y == cls]
            self.mean[cls] = X_cls.mean(axis=0)
            self.variance[cls] = X_cls.var(axis=0) + self.epsilon  # Varyansa epsilon ekle
            self.priors[cls] = X_cls.shape[0] / X.shape[0]

    def _gaussian_probability(self, x, mean, variance):
        # Gaussian dağılım formülü
        exponent = np.exp(-((x - mean) ** 2) / (2 * variance))
        return (1 / np.sqrt(2 * np.pi * variance)) * exponent

    def _calculate_class_probabilities(self, x):
        probabilities = {}
        for cls in self.classes:
            prior = np.log(self.priors[cls])
            likelihood = np.sum(
                np.log(self._gaussian_probability(x, self.mean[cls], self.variance[cls]))
            )
            probabilities[cls] = prior + likelihood
        return probabilities

    def predict(self, X):
        predictions = []
        for x in X:
            class_probs = self._calculate_class_probabilities(x)
            predictions.append(max(class_probs, key=class_probs.get))
        return np.array(predictions)


# Veri setinin yüklenmesi
data1 = pd.read_csv("C:/Users/ahmet/PycharmProjects/PythonProject3/data.csv")

# Veriyi ön işleme
data1.drop(['Unnamed: 32', 'id'], axis=1, inplace=True)
data1['diagnosis'] = data1['diagnosis'].map({'B': 0, 'M': 1})  # Etiketleme

# Özellikler ve hedef değişken
X = data1.drop('diagnosis', axis=1).to_numpy()
y = data1['diagnosis'].to_numpy()

# Eğitim ve test setlerine bölme
train_size = int(0.8 * X.shape[0])
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Gaussian Naive Bayes modelini oluşturma ve eğitme
model = GaussianNaiveBayes()
start_train = time.time()
model.fit(X_train, y_train)
end_train = time.time()

# Model tahmini
start_predict = time.time()
y_pred = model.predict(X_test)
end_predict = time.time()

# Performans metrikleri
accuracy = np.mean(y_pred == y_test)
conf_matrix = np.zeros((2, 2), dtype=int)
for true, pred in zip(y_test, y_pred):
    conf_matrix[true, pred] += 1

# Eğitim ve tahmin süreleri
training_time = end_train - start_train
prediction_time = end_predict - start_predict

# Karmaşıklık matrisini görselleştirme
plt.figure(figsize=(8, 6))
plt.imshow(conf_matrix, interpolation='nearest', cmap=plt.cm.Blues)
plt.title("Confusion Matrix - Custom Gaussian Naive Bayes")
plt.colorbar()

# Etiketler
classes = ['Benign (0)', 'Malignant (1)']
tick_marks = np.arange(len(classes))
plt.xticks(tick_marks, classes, rotation=45)
plt.yticks(tick_marks, classes)

# Matris değerlerini görselleştirme
thresh = conf_matrix.max() / 2.0
for i, j in np.ndindex(conf_matrix.shape):
    plt.text(j, i, format(conf_matrix[i, j], 'd'),
             horizontalalignment="center",
             color="white" if conf_matrix[i, j] > thresh else "black")

plt.ylabel('True Label')
plt.xlabel('Predicted Label')
plt.tight_layout()
plt.show()

# Sonuçları yazdırma
print(f"Eğitim Süresi: {training_time:.4f} saniye")
print(f"Tahmin Süresi: {prediction_time:.4f} saniye")
print(f"Doğruluk (Accuracy): {accuracy:.2%}")

