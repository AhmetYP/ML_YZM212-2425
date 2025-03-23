# YZM212 MACHINE LEARNING DERSI 2. LAB PROJESI

## 1. Giriş
Bu proje, **lojistik regresyon kullanarak ikili sınıflandırma** yapmayı amaçlamaktadır. Projede **iki farklı model** oluşturulmuştur:

1. **Scikit-learn kullanarak Logistic Regression modeli**
2. **Scikit-learn kullanmadan, sıfırdan yazılan Logistic Regression modeli**

Bu README dosyasında, **iki modelin teorik karşılaştırması, performans analizi ve değerlendirme metrikleri** detaylıca ele alınmıştır.

---

## 2. Veri Seti ve Veri Önişleme

Kullanılan veri seti **9000 örnek ve en az 5 özellik içermektedir**. İşlemler sırasında:
- Eksik veriler temizlenmiştir.
- Kategorik değişkenler one-hot encoding ile sayısal hale getirilmiştir.
- Veri seti **eğitim (%80) ve test (%20)** olarak ikiye ayrılmıştır.

---

## 3. Teorik Karşılaştırma

| **Özellik**                | **Scikit-learn Modeli**                                   | **Sıfırdan Yazılan Model**                     |
|----------------------|------------------------------------------------|-----------------------------------|
| **Optimizasyon**       | LBFGS (Varsayılan) veya SGD gibi hazır algoritmalar kullanır. | Gradient Descent (Elle kodlandı)  |
| **Hesaplama Hızı**    | Daha hızlı, çünk optimize edilmiş kütüphaneler kullanıyor. | Daha yavaş, çünk numpy ile manuel hesaplamalar yapılıyor. |
| **Eğitim Yöntemi**      | Otomatik **durma kriterleri** ile optimize edilir. | Manuel olarak belirlenen iterasyon sayısı kullanılır. |
| **Maliyet Fonksiyonu** | Maksimum Likelihood Estimation (MLE) kullanılır. | Aynı MLE fonksiyonu kullanılıyor. |
| **Hassasiyet**       | Daha iyi çünk çeşitli optimizasyon teknikleri uygular. | Biraz daha düşük olabilir. |

---

## 4. Performans Karşılaştırması

**Model 1: Scikit-learn Kullanılan Logistic Regression**
- **Doğruluk (Accuracy):** 0.8944
- **Eğitim Süresi:** 0.0471 saniye
- **Test Süresi:** 0.0007 saniye

**Model 2: Elle Yazılan Logistic Regression**
- **Doğruluk (Accuracy):** 0.8886
- **Eğitim Süresi:** 1.5525 saniye
- **Test Süresi:** 0.0012 saniye

Görüldüğü gibi, **Scikit-learn modeli daha hızlı ve biraz daha doğrudur.** Bu, hazır kütüphanelerin optimize edilmiş olmasından kaynaklanmaktadır.

---

## 5. Karmaşıklık Matrisi ve Değerlendirme Metrikleri

Karmaşıklık matrisi, modelin hangi tür hata yaptığını anlamamızı sağlar.

### **Scikit-learn Logistic Regression Modeli Karmaşıklık Matrisi**
```
               precision    recall  f1-score   support

           0       0.93      0.94      0.93      6990
           1       0.78      0.74      0.76      2010
```

### **Elle Yazılan Logistic Regression Modeli Karmaşıklık Matrisi**
```
               precision    recall  f1-score   support

           0       0.93      0.93      0.93      6990
           1       0.75      0.74      0.75      2010
```

---

## 6. Değerlendirme Metrikleri

| **Metrik**  | **Açıklama**  |
|------------|---------------------------------------------------------------|
| **Doğruluk (Accuracy)** | Modelin toplam doğruluk oranıdır. |
| **Kesinlik (Precision)** | Pozitif tahminlerin ne kadar doğru olduğunu gösterir. |
| **Duyarlılık (Recall)** | Gerçek pozitiflerin ne kadar doğru yakalandığını gösterir. |
| **F1-Skoru** | Precision ve Recall arasında denge kuran metriktir. |

---

## 7. Sonuçlar ve Tartışma

1. **Scikit-learn modeli, elle yazılan modele göre daha başarılı ve daha hızlıdır.** Bunun sebebi **LBFGS gibi optimize edilmiş algoritmaların kullanılmasıdır.**
2. **Elle yazılan model, lojistik regresyon algoritmasını anlamak için faydalıdır.** Ancak pratikte, hazır kütüphanelerin kullanılması önerilir.
3. **Model değerlendirmesinde sadece doğruluk metriğine bakmak yeterli değildir.** Precision, recall ve F1-score gibi ek metrikler de incelenmelidir.
4. **Eğer sınıf dağılımı dengesizse, recall ve precision daha fazla önem kazanır.**

Bu \e7alışma, **Scikit-learn kullanarak model geliştirmenin avantajlarını gösterirken, lojistik regresyonun temel prensiplerini anlamamıza da yardımcı olmaktadır.** 🚀

