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












