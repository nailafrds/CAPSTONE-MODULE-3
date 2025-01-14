link vid: https://drive.google.com/drive/folders/14Up4qkSOMTKxIe56UMLngyDYI7losxHa?usp=share_link
# **Capstone Module 3 : Saudi Arabia Used Cars**

## **Contents**

1. Business Problem Understanding
2. Data Understanding
3. Data Preprocessing
4. Modeling
5. Conclusion
6. Recommendation

****

### **Context**


Mobil merupakan sarana transportasi manusia, seiring perkembangan zaman manusia semakin membutuhkan adanya mobil untuk berkegiatan sehari-hari, namun rata rata harga mobil saat ini terbilang cukup tinggi sehingga banyak orang lebih memilih membeli mobil bekas dariapada membeli mobil baru untuk di gunakan sehari-hari.

Saudi Arabia sebagai salah satu negara yang menyediakan market jual beli mobil bekas dengan jumlah yang cukup tinggi. Segemntasi marketnya pun terbagi bagi:
1. Berdasarkan jenis kendaraan (SUV,MPV,sedan dan hattback)
2. Berdasarkan penjualan (online dan offline)

Di landir dari laman `mordorintelligence.com` analisi penjualanan mobil bekas pada tahun 2024 diperkirakan mencapai USD 6,41 miliar faktor-faktor seperti peningkatan kualitas mobil bekas, banyaknya ekspatriat, dan harga yang terjangkau untuk mobil bekas diperkirakan akan menjadi faktor pendorong utama pasar. Dan juga kontribusi platform online sangat berpengaruh pada pertumbuhan penjualanan karena sebanyak 98.6% penduduk arab saudi telah menggunakan internet, sehingga dengan adanya platform digital ini mendorong penjual untuk memperlihatkan mobil bekas mereka cukup dengan memberi gambar dan juga informasi kondisi mobil seperti  tipe mobil,merk, tahun produksi, jarak tempuh mobil dll,
sehingga memudahkan konsumen untuk mengetahui dan berinteraksi dengan penjual. Salah satu platform nya yitu `syarah.com` menyediakan jasa jual beli mobil bekas dengan berbagai macam merk

### **Problem Statement**

Salah satu tantangan terbesar bagi pengusaha jual beli mobil bekas baik bebasis offline maupun online adalah masih kurangnya kepercayaan konsumen terhadap mobil bekas sehingga hal tersebut terkadang menyebabkan penjual sulit untuk menentukan harga jual.

Karena mobil bekas sendiri sangat banyak di pasaran dengan harga yang kompetitif namun disamping itu mobil bekas sendiri pasti memiliki kekurangan meski sedikit dan ini sangat menjadi pertimbangan bagi pembeli untuk memilih dan juga bagi penjual ketika menentukan harga

Oleh karena itu perlu adanya sebuah tumpuan bagi penjual untuk menentukan harga yang tetap sehingga pembeli tidak sulit untuk mempertimbangkan mobil tersebut.

### **Goals**

Berdasarkan permasalahn tersebut, penjual mobil bekas memerlukan sebuah alat yang dapat **membantu penjual untuk menentukan harga jual yang sesuai untuk semua jenis mobil yang akan mereka jual**. Dengan bantuan pengetahuan mengenai kondisi mobil tersebut seperti tipe mobil, mesin, tahun produksi, jarak tempuh mobil, akan mendapatkan sebuah prediksi harga yang lebih akurat sehingga penjual tidak perlu kesulitan lagi untuk menentukan harga.

Dengan adanya prediksi harga yang lebih akurat membuat konsumen menumbuhkan kepercayaan mereka terhadap penjual karena harga ditentukan berdasarkan kondisi mobil dan juga membantu konsumen yang kurang mengerti mengenai mobil, oleh karena itu apabila konsumen semakin tumbuh kepercayaan nya maka penjualan akan meningkat karena konsumen tidak banyak mempertimbangkan kondisi mobil dan juga terhindar 

### **Analytic Approach**

Setelah menentukan problem statement kita perlu adanya analisis data untuk menentukan fitur fitur atau bagian bagian mobil mana yang dapat di jadikan jalan untuk membuat alat tersebut.


Dan setelahnya kita akan membentuk sebuah model regresi yang akan membantu penjual untuk membuat alat yang dapat memprediksi harga jual mobil dan ini berguna untuk penjual untuk menentukan harga jual yang sesuai dengan kondisi mobil.

### **Metric Evaluation**

Pada percobaan machine learning kali ini menggunakan 3 evaluasi metrik yaitu **RMSE, MAE, MAPE**, ketiga metrik tersbut bertujuan untuk melihat nilai eror pada prediksi/ramalan yang telah di buat.

- RMSE atau Root Mean Square Error sebuah metrik untuk mengukur besaran nilai eror semakin kecil nilai nya atau mendekati 0 makan semakin akurat prediksi nya namun jarang sekali niali rmse yang dapat mencapai 0 karena setiap prediksi pasti terdapat kesalahan, metrik ini juga sangat penting karena mempunyai sensitivitas terhadap outliers sehingga memudahkan untuk mengidentifikasi outliers.

- MAE atau mean absolute error, kergunaan nya untuk  perbedaan rata rata dari nilai prediksi dan nilai aktual, memiliki sifat yang sama seperti rmse yaitu semakin kecil nilai nya maka semakin akurat modelnya namun metrik mae ini tidak terlalu sesitif terhadap outliers. Metriks ini juga penting untuk mengur regresi dan distribusi frekuensinya.

- MAPE atau mean percentage error, merupakan metrik untk menghitung rata rata dari selisih persentase anatar nilai prediksi dan aktual sama seperti kedua metrik yang sudah di jelaskan, mape semakin akurat jika nilainya semakin kecil, dna mape juga sangat sensitif terhadap nilai yang sangat kecil, metrik ini sangat cocok untuk permasalahan bisnis terutama untuk prediksi penjualanan atau arus kas serta mudah dipahami karena berbentuk persentase.

Dengan ini ketiga metrik tersebut dianggap cocok untuk permasalahan bisnis yang telah dijelaskan.
