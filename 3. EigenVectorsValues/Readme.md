# MATRIX MANIPULATIONS

## Matris Nedir?
  Matris, sayılardan oluşan dikdörtgen şeklinde bir tabloya verilen isimdir. Bu tablo satır (row) ve sütunlardan (column) oluşur. Genellikle büyük harflerle (A,B,M) ile gösterilir.
 
  A = ((a11, a12), (a21,a22), (a31, a32)) şeklinde veya 

![image](https://github.com/user-attachments/assets/ef9bf8cf-c056-4bea-af8a-57d3468dbe73) olarak gösterilebilir.


## Matris Türleri

### Scalers
Başlamak için önce bir skaler tanımlayalım. Skaler, gerçek ya da karmaşık tek bir sayıdır. -6 veya 3 gibi. Geleneksel olarak, skalerler için değişken adları küçük harfle yazılır ve kalın harflerle yazılmaz.


### Vectors
Bir vektör, skalerlerin satır veya sütun şeklinde düzenlenmiş bir koleksiyonudur. Bizim kullanacağımız gösterim biçimi, vektörlerin kalın yazılmış küçük harflerle gösterilmesi olacaktır.

![image](https://github.com/user-attachments/assets/72c46c33-32bd-45c1-87d7-b75d9d219329)

### Matrix
Nasıl ki bir vektör, skalerlerin bir koleksiyonuysa, bir matris de (hepsi aynı uzunlukta olan) vektörlerin bir koleksiyonu olarak görülebilir. Matrisleri kalın ve büyük harflerle göstereceğiz.

Satır sayısının sütun sayısına eşit, daha az ya da daha fazla olması gibi bir zorunluluk yoktur. Bir matrisin boyutunu belirtirken önce satır sayısını, sonra sütun sayısını yazarız

### Kare Matris
Kare matris, sütunlarla aynı sayıda satıra sahip bir matristir. 

![image](https://github.com/user-attachments/assets/e58cefd5-9642-42aa-869c-3dad98e8bbcc)


### Simetrik Matris
Bir simetrik matris, kare (satır sayısı sütun sayısına eşit) bir matristir ve matrisin i,j elemanı, j,i elemanına eşittir. Yani, bir matris A simetrik ise Transpoze'u ile kendisi aynıdır.

![image](https://github.com/user-attachments/assets/5ac52b63-3e83-4785-8c24-afe71a54f7fe)


### Diagonal Matris
Ana köşegeni dışındaki tüm elemanları sıfır olan kare matrislere köşegen matris (diagonal matrix) denir.

![image](https://github.com/user-attachments/assets/2997b662-66b8-4d9b-be0e-e858ebae0485)


### Birim Matris 
Ana köşegenindeki tüm değerler tam olarak 1 olan bir köşegen matrise birim matris (identity matrix) denir.

![image](https://github.com/user-attachments/assets/2c610b8f-1dbb-42c5-aa1e-bdff7e65efdf)



## OPERATIONS ON MATRICES

### Transpoze
Bir matrisin transpozu, satır ve sütunlarının yer değiştirmesiyle elde edilen yeni bir matristir. Yani bir matrisin transpozunu aldığımızda:

İlk satır, ilk sütun olur. İkinci satır, ikinci sütun olur.

![image](https://github.com/user-attachments/assets/55a58ec2-8c3c-4471-9335-87ec059bd4a3)

### Addition and Subtraction
Toplama ve çıkarma işlemleri eleman bazında (element-wise) yapılır.
Yani iki matrisin veya vektörün toplanabilmesi ya da çıkarılabilmesi için boyutlarının (satır ve sütun sayılarının) birebir aynı olması gerekir.

![image](https://github.com/user-attachments/assets/703df4c9-0f85-49d9-9545-76f9c07bd9e4)

### Matrix Multiplication (Hadamard Product)
Aynı boyuta sahip iki matris birbirleriyle çarpılabilir ve bu genellikle eleman bazında matris çarpımı veya Hadamard çarpımı olarak adlandırılır.
Bu, matris çarpımı denildiğinde kastedilen tipik işlem değildir, bu nedenle genellikle farklı bir operatör kullanılır, örneğin daire şeklinde bir "o" sembolü.

C = A o B

![image](https://github.com/user-attachments/assets/1280badb-0da1-4746-a72e-403e69c3eb44)

### Matrix-Matrix Multiplication (Dot Product)
Eğer X bir m x n boyutunda bir matris ve W bir n x p boyutunda bir matris ise, o zaman Z = XW çarpımı, m x p boyutunda bir matris olur.
Bu çarpımda, her bir eleman z(i,j), X matrisinin i-inci satırı ile W matrisinin j-inci sütununun skaler çarpımına eşittir.

Çarpılacak matrislerin boyutları uygun olmalıdır. Yani, X matrisinin sütun sayısı ile W matrisinin satır sayısı eşit olmalıdır.

![image](https://github.com/user-attachments/assets/fd25d9b3-5018-411b-b54b-cc59547572b4)

### Scaler times a Matrix
Matematiksel olarak, bir matrisi bir skalerle çarpmak, boyutlar uyumsuz olduğu için doğrudan mümkün değildir. Ancak, bazen yazım açısından kolaylık sağladığı için bu işlem kullanılabilir.

![image](https://github.com/user-attachments/assets/9c682f45-4887-40ee-be12-43c77a2fb782)


# EIGENVECTORS AND EIGENVALUES

## Eigendecomposition
Eigendecomposition, bir matrisin özdeğerler (eigenvalues) ve özvektörler (eigenvectors) kullanılarak ayrıştırılması işlemidir. Bu işlem, lineer cebir ve makine öğrenmesinde çok önemli bir yer tutar. Özellikle veri analizi, boyut indirgeme, ana bileşen analizi (PCA) gibi yöntemlerde kullanılır.

Bir vektör, aşağıdaki denklemi sağlıyorsa bir matrisin özvektörüdür.

A . v = lambda . v

Buna özdeğer denklemi denir, burada A, ayrıştırdığımız ana kare matrisidir, v matrisin özvektörüdür ve lambda, küçük Yunan harfi olup özdeğer skalerini temsil eder.

Bir matris, ana matrisin her bir boyutu için bir özvektör ve bir özdeğere sahip olabilir. Ancak her kare matris özvektörlere ve özdeğerlere ayrıştırılamaz; bazıları ise yalnızca karmaşık sayılar kullanılarak ayrıştırılabilir. Ana matris, özvektörler ve özdeğerlerin bir çarpımı şeklinde ifade edilebilir.

A = Q . diag(V) . Q^-1

Burada Q, özvektörlerden oluşan bir matristir; diag(V), köşegeninde özdeğerlerin bulunduğu bir diagonal (köşegen) matristir (bazen büyük lambda harfi ile gösterilir); Q⁻¹ ise özvektörlerden oluşan matrisin tersidir.

Bir ayrıştırma (decomposition) işlemi, matrisi sıkıştırmaz; bunun yerine matrisi, belirli işlemleri daha kolay gerçekleştirebilmek için temel bileşenlerine ayırır. Diğer matris ayrıştırma yöntemlerinde olduğu gibi, Eigendecomposition (özdeğer ayrıştırması) da daha karmaşık matris işlemlerinin hesaplanmasını kolaylaştırmak amacıyla kullanılan bir araçtır.


## Eigenvectors and Eigenvalues

Özvektörler, birim vektörlerdir; yani uzunlukları ya da büyüklükleri 1.0’a eşittir.

Özdeğerler ise özvektörlere uygulanan katsayılardır ve bu katsayılar, vektörlerin uzunluğunu ya da büyüklüğünü belirler.

## Calculation of Eigendecomposition
Eigendecomposition, kare bir matris üzerinde, detaylarına girmeyeceğimiz verimli bir yinelemeli algoritma ile hesaplanır.

Genellikle önce bir özdeğer bulunur, ardından bu özdeğere karşılık gelen özvektörü bulmak için denklemin katsayıları çözülür.

NumPy kütüphanesinde bu ayrıştırma, eig() fonksiyonu kullanılarak hesaplanabilir.

![image](https://github.com/user-attachments/assets/59d63c3f-2101-4188-b7f7-319f3d547550)


# RELATIONS WITH MACHINE LEARNING
Makine öğrenmesinde matris manipülasyonu, eigenvalues ve eigenvectors çok temel kavramlardır. Bu kavramlar veriyi anlamlandırmak, boyutunu azaltmak, paternleri keşfetmek ve modelleri daha verimli hale getirmek için kullanılır.

Makine öğrenmesinde veriler genellikle matrisler halinde düzenlenir. Bu matrislerin yapısı şu şekildedir:
Satırlar, her biri bir veri örneğini temsil eder (örneğin bir resim, bir metin parçası, bir müşteri bilgisi vb.). Sütunlar ise her biri bir özelliği (feature) temsil eder (örneğin bir pikselin renk değeri, bir kelimenin sıklığı, yaş, maaş gibi bilgiler).

Matrisler sayesinde hızlı hesaplamalar yapılabilir (toplama, çarpma, transpoz vb.). Veri dönüşümleri kolaylaşır (ölçekleme, döndürme, boyut indirgeme). Öğrenme algoritmaları bu yapılar üzerinde verimli şekilde çalışır.

Makine öğrenmesi modelini eğitirken, giriş verileri (örneğin resimler veya metin) ağırlıklarla (modelin desenleri öğrenmek için kullandığı değerler) matris çarpımından geçer. Bu süreç, yapay zekanın giriş verisi ile çıkış tahminleri arasındaki ilişkileri tanımasına yardımcı olur.

Matrisler, büyük ve karmaşık veri setlerini daha işlem yapılabilir küçük parçalara ayırmaya yardımcı olur.

Matris çarpımı, makine öğrenmesi modellerinin karmaşık desenleri tanımlamasını sağlar.
Bu matrisler eğitim sırasında güncellenerek yapay zeka sisteminin sürekli olarak iyileşmesini ve daha doğru hale gelmesini sağlar.

Eigenvectors ve eigen values, bir matrisin iç yapısını tanımlar. Makine öğrenmesinde genellikle veriler matrislere dönüştürülür ve bu matrisler üzerinde çeşitli dönüşümler gerçekleştirilir. Bu dönüşümlerin doğasını anlamak için eigendecomposition veya benzeri matris faktorizasyon teknikleri kullanılır.


## Makine Öğrenmesinde Özdeğerler ve Özvektörlerin Kullanımı

### 1. PCA (Principal Component Analysis - Temel Bileşen Analizi):  
Özdeğerler ve özvektörler, PCA algoritmasında temel bileşenleri (verinin en fazla varyansı gösteren yönleri) bulmak için kullanılır. Bu yöntem, veriyi daha düşük boyutlu bir alana indirgerken, önemli bilgiyi korumaya yardımcı olur.

### 2. Image Compression: 
Özvektörler, verinin en önemli bileşenlerini temsil eder, bu nedenle gereksiz verileri elemek ve veriyi sıkıştırmak için kullanılabilir. Bu, belleği verimli kullanmayı sağlar.

Özvektörler ve özdeğerler, Görüntü Sıkıştırma için Tekil Değer Ayrıştırması (SVD) gibi tekniklerde kullanılır. Görüntüleri, özvektörler ve özdeğerler cinsinden temsil ederek, depolama gereksinimlerini azaltabilir ve temel görüntü özelliklerini koruyabilirsiniz.

### 3. Support Vector Machines: 
SVM, sınıflandırma ve regresyon görevleri için kullanılabilen bir makine öğrenmesi algoritmasıdır. SVM'ler, veriyi iki sınıfa ayıran bir hiper düzlem bulmaya çalışır. SVM'nin çekirdek matrisinin özdeğerleri ve özvektörleri, algoritmanın performansını artırmak için kullanılabilir

### 4. Graph Theory: 
Eigenvectors, networkler ve graphların analizinde önemli bir rol oynar. 
Sosyal networklerde veya diğer birbirine bağlı sistemlerde önemli düğümleri veya toplulukları bulmak için kullanılabilirler.

### 5. Natural Language Processing (NLP): 
NLP alanında özvektörler büyük bir belge-terim matrisindeki en ilgili terimleri belirlemeye yardımcı olabilir. Bu, belge alma ve metin özetleme  gibi tekniklerin kullanılmasını sağlayan Latent Semantic Analysis (LSA) gibi yöntemlere olanak tanır.




# numpy.linalg.eig
  Bu function input olarak verilen kare matrisin eigenvalues ve right eigenvectors hesaplar.
## Dokümantasyon  
 a : (..., M, M) array    PARAMETERS
 > Girdi olarak verilen veri tipi, liste, matris ya da başka bir şey olabilir ama eig fonksiyonu bunu NumPy dizisine çevirir.
 
 > (M,M) bu ifade  matrisin kare matris olması gerektiğini gösterir.

> (...,) Bu, "broadcasting" ile çok boyutlu matris kümelerinin (batch) desteklendiğini gösterir yani birden fazla kare matristen oluşan bir dizi input olabilir.

 Returns

Fonksiyon bize bir namedtuple döndürüyor. Bu yapı aslında, birden fazla değeri isimlendirilmiş olarak döndürmenin şık bir yolu. Burada dönen tuple iki şey içeriyor:

1) eigenvalues , 2) eigenvectors

 eigenvalues : (..., M) array
 > Matrisin özdeğerlerini tutan NumPy dizisidir. 

> Eğer bir özdeğer birden fazla kez çıkıyorsa, bu tekrar edilir.

> Özdeğerler büyüklük sırasına göre dizilmez. Sıra rastgele olabilir.

> Sonuçlar kompleks sayı (complex128) olabilir. Ama eğer özdeğerlerin imajiner kısmı sıfırsa, otomatik olarak gerçek sayıya (float64) dönüştürülür.

> Eğer a matrisi gerçek (real) sayılardan oluşuyorsa:
>
> Özdeğerler gerçek olabilir veya Veya kompleks eşlenik çiftleri halinde çıkabilir (örneğin 1 + 2j , 1 - 2j)

eigenvectors : (..., M, M) array
> Matrisin özvektörlerini tutan NumPy dizisidir.

> Her sütun, bir özvektördür.
>
> Yani eigenvectors[:, i] → eigenvalues[i] özdeğerine karşılık gelen özvektördür.

> Özvektörler normalize edilmiştir.


 Raises
    ------
    LinAlgError

 Bu bölüm, fonksiyonun hata (exception) durumlarını anlatır.

 >Python'da bir fonksiyon çalışırken beklenmeyen bir durumla karşılaşırsa, bir hata (exception) fırlatır.
Raises başlığı da bu fonksiyonun hangi durumda hata vereceğini açıklar.

>Eğer bu algoritma yaklaşım yoluyla özdeğeri bulmakta zorlanırsa, "converge etmedi" der ve LinAlgError fırlatır.

```python
a, wrap = _makearray(a)
```
>Giriş olarak verilen a matrisini NumPy dizisine çeviriyor.

```python
>wrap, çıktıların şeklinin girişle aynı formatta kalmasını sağlamak için kullanılıyor
```
```python
_assert_stacked_square(a)
```
> Giriş matrisinin kare olup olmadığını kontrol eder.
```python
_assert_finite(a)
```
> Matriste sonsuz (inf) ya da tanımsız (NaN) değer var mı? diye kontrol eder.
```python
t, result_t = _commonType(a)
```
> a matrisinin veri tipine (float32, complex64, float64, vs.) bakar. Sayısal işlemler için uygun ortak bir tür belirler.
>
>  Örnek: float matrisle complex bir matris birlikte işlem görüyorsa, sonuç complex olmalıdır.
```python
signature = 'D->DD' if isComplexType(t) else 'd->DD'
```
>LAPACK, özdeğer ve özvektör hesaplamaları gibi işlemleri gerçekleştiren bir kütüphanedir ve "signature" parametresi bu fonksiyonların hangi türde veri alıp vereceğini belirtir.
>
>isComplexType(t)
>
>Bu fonksiyon, matrisin veri tipini kontrol eder ve complex (karmaşık) sayı içerip içermediğini belirler. Eğer complex sayı içeriyorsa True döndürecektir.

>'D->DD' Bu imza, karmaşık sayılarla çalışıldığını ve sonuçların karmaşık sayılar olacağını belirtir.

>Bu imza, girişin gerçek sayılar içerdiğini ama yine de karmaşık sayılarla çalışılacağını belirtir.
>
>Eğer karmaşık sayılar varsa (isComplexType(t) True dönerse), signature 'D->DD' olur. Yani karmaşık sayılarla işlem yapılacak.
>
>Eğer gerçek sayılar varsa, signature 'd->DD' olur. Burada karmaşık sayılara dönüştürülerek işlem yapılır.


```python
with errstate(call=_raise_linalgerror_eigenvalues_nonconvergence, 
              invalid='call', over='ignore', divide='ignore', 
              under='ignore'):
    w, vt = _umath_linalg.eig(a, signature=signature
```
errstate() Nedir?
>errstate() fonksiyonu, hata durumlarını yönetmek için kullanılır.

errstate() Parametreleri
call=_raise_linalgerror_eigenvalues_nonconvergence:

>_raise_linalgerror_eigenvalues_nonconvergence: Bu özel hata fonksiyonu, özdeğerlerin hesaplanamaması durumunda çağrılır ve hata mesajı verir.

invalid='call'
>Sayısal bir işlem geçersiz olduğunda, örneğin "NaN" (Not-a-Number) bir değerle karşılaşıldığında, hata meydana gelir. Bu durumda işlem call olarak yönetilir ve fonksiyon çağrılır.

over='ignore'
>Bu parametre, aşırı büyük sayılar (overflow) ile karşılaşıldığında işlem yapılmasına izin verir, yani overflow hatası olsa bile işlem yapılır ve bir hata mesajı verilmez.

divide='ignore'
>Bu parametre, sıfıra bölme durumunu yönetir. Eğer sıfıra bölme olursa, hata yerine işlem yapılır ve sonuç bilinmeyen bir değeri (örneğin, inf veya NaN) döndürebilir.

under='ignore'
>Bu, aşırı küçük sayılar (underflow) ile karşılaşıldığında ne yapılacağını belirtir. Bu durumda işlem yapılır ve sonuç düşük hassasiyetle elde edilebilir.

_umath_linalg.eig(a, signature=signature) Fonksiyonu
>_umath_linalg.eig fonksiyonu, LAPACK'ın alt modüllerinden biri olan eig fonksiyonunu çağırır. Bu fonksiyon, giriş matrisinin özdeğerlerini (w) ve özvektörlerini (vt) hesaplar.
>
>w: Özdeğerleri içeren bir vektördür.
>vt: Özvektörlerin sütunlar halinde olduğu bir matrisi döndürür.

```python
if not isComplexType(t) and all(w.imag == 0.0):
    w = w.real
    vt = vt.real
    result_t = _realType(result_t)
else:
    result_t = _complexType(result_t)
```
if not isComplexType(t) and all(w.imag == 0.0)
>Bu satır, özellikle özdeğerler ve özvektörlerle çalışırken veri türünü kontrol etmek ve gerektiğinde dönüşüm yapmak için kullanılır.
>
>w.imag == 0.0 kısmı tüm özdeğerlerin karmaşık kısmını 0 olup olmadığını kontrol eder.

w = w.real ve vt = vt.real
> Karmaşık olan kısımları varsa eğer bu işlemle beraber sadece reel kısımları alınır.

result_t = _realType(result_t)
>Burada, result_t değişkeninin tipi gerçek sayılar (real numbers) olarak değiştirilir.

else: result_t = _complexType(result_t)
>Eğer önceki if koşulu sağlanmazsa (yani, özdeğerler karmaşık sayılarsa), result_t karmaşık sayılar olacak şekilde güncellenir.
```python
vt = vt.astype(result_t, copy=False)
```
> Özvektör matrisini, daha önce belirlenen result_t tipine dönüştürüyor.

```python
return EigResult(w.astype(result_t, copy=False), wrap(vt))
```
>w ve vt'yi EigResult adında bir namedtuple yapısına koyarak döndürüyor. w = eigenvalues, vt = eigenvectors
>
>wrap(vt) → Çıktı formatı, girişle aynı düzeni korusun diye uygulanır.


1. Girdiyi düzenle
2. Kare matris mi, sonlu mu? → kontrol et
3. Veri tipi belirle
4. LAPACK fonksiyonu ile özdeğer ve özvektör hesapla
5. Gerekirse complex → real dönüşüm yap
6. Sonucu uygun formatta döndür




