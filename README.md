# ML_YZM212-2425
# Değerlendirme Metrikleri

## Accuracy (Doğruluk)

**Tanımı:**  
Doğru tahmin edilen örneklerin toplam tahmin edilen örneklere oranıdır.

**Formül:**  
\[ Accuracy = \frac{\text{Doğru Tahminler}}{\text{Toplam Tahminler}} \]

**Gözlemler:**  
- Scikit-learn modeli için doğruluk: **%97.37**  
- Manuel model için doğruluk: **%92.11**  
- Scikit-learn modeli daha yüksek doğruluk sağlamıştır.  

**Not:**  
Doğruluk metriği, dengesiz veri setlerinde yanıltıcı olabilir. Örneğin, çoğunluk sınıfını sürekli tahmin eden bir model yüksek doğruluk verebilir.

---

## Confusion Matrix (Karmaşıklık Matrisi)

**Tanımı:**  
Tahmin edilen ve gerçek değerlerin bir tablo olarak sunulmasıdır. Şu bileşenlerden oluşur:
- **True Positive (TP):** Doğru şekilde "pozitif" olarak tahmin edilen örnekler.
- **True Negative (TN):** Doğru şekilde "negatif" olarak tahmin edilen örnekler.
- **False Positive (FP):** Yanlış bir şekilde "pozitif" olarak tahmin edilen negatif örnekler.
- **False Negative (FN):** Yanlış bir şekilde "negatif" olarak tahmin edilen pozitif örnekler.

**Gözlemler:**  
- Scikit-learn modeli, hem benign (iyi huylu) hem de malignant (kötü huylu) sınıfları daha tutarlı bir şekilde tahmin etmiştir.  
- Manuel model, malignant (1) sınıfında daha fazla hata yapmıştır. Bu, dengesiz sınıf dağılımı durumunda performans kaybına neden olabilir.

---

## Sonuç

- **Scikit-learn modeli**, genel doğruluk ve sınıflar arası denge açısından daha iyi performans göstermiştir.
- **Manuel model**, varyans sıfır olduğunda yapılan optimizasyonlarla bir derece iyileştirilmiş olsa da, sınırlamaları devam etmektedir.

**Değerlendirme Metriklerinin Seçimi:**  
Tıbbi tanı problemlerinde, sınıf dengesizliklerini ve yanlış negatiflerin önemini göz önünde bulundurarak **F1-Score**, **Recall** ve **Precision** gibi metrikler tercih edilmelidir. Confusion matrix, bu metrikleri detaylı bir şekilde analiz etmeyi mümkün kılar.
