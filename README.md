[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/uiI2_xo4)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15220917&assignment_repo_type=AssignmentRepo)

# Introduction
=================================================================================================================================================

Group 2

Batch : 030 RMT

Data Analyst   : Rizky Chester Abadi, Ranie Sita Mannuela.

Data Scientist : Raymond Samuel, Raodah Hasman.

Data Engineer  : Raymond Samuel.

* Dataset Source: https://archive.ics.uci.edu/
* Dataset name  :user_behavior.csv, user_profile.csv

#### Latar belakang: 
* Penggunaan E-Commerce telah meningkat pesat dalam beberapa tahun terakhir, menciptakan peluang besar di pasar. Namun, tingkat konversi pembelian tidak meningkat dengan kecepatan yang sama, sehingga diperlukan solusi yan dapat memberikan promosi yang dipersonalisasi kepada pembeli online. Dalam perdagangan fisik, seorang penjual dapat menawarkan berbagai alternatif yang disesusaikan kepada pembeli berdasarkan pengalaman yang telah diperolehnya. Pengalaman ini sangat mempengaruhi efisiensi waktu, tingkat konversi pembelian, dan angka penjualan.

* Banyak perusahaan E-Commerce dan teknologi informasi menginvestasikan sumber daya untuk mengembangkan sistem deteksi dini dan prediksi perilaku yang meniru perilaku penjual pada lingkungan belanja virtual. Beberapa studi akademis juga telah mengusulkan berbagai metode machine learning untuk menangani  masalah terseubt dari berbagai perspektif. Beberapa studi berfokus pada pengelompokkan kunjungan berdasarkan pola navigasi pengguna, sementara yang lain bertujuan untuk memprediksi perilaku pengguna secara in time untuk mengamil tindakan yang tepat guna meningkatkan tingkat penyelesaian transaksi dan mengurangi tingkat pengabaian keranjang belanja.


#### SMART framework
* Spesific      : Memprediksi konversi pengunjung situs E-Commerce berdasarkan perilaku browsing
* Measurable    : Mengukur tingkat akurasi mencapai 80% pada model prediksi konversi pengunjung
* Achieveable   : Mengembangkan dan mengimplementasikan model prediksi menggunakan data historis pengunjung
* Relevant      : Mendukung keputusan bisnis untuk meningkatkan konvesi dan retensi pelanggan
* Time bound    : Mencapai model prediksi dengan akurasi tinggi dalam 1 minggu

#### Identifikasi Masalah :
1. Bagaimana kategori berdasarkan jenis pengunjung dari setiap wilayah?
2. Apa kategori sistem operasional yang digunakkan oleh pengguna?
3. Bagaimana kategori berdasarkan banyaknya pengguna yang membeli dari tiap region
4. Bagaimana distribusi jumlah halaman produk yang dikunjungi pengguna?
5. Apakah ada hubungan antara durasi di halaman administratif dan bounce rates?
6. Fitur apa yang paling berpengaruh terhadap pendapatan?
7. Analisis deskriptif : Bagaimana analisi distribusi nilai halaman produk dan analisis durasi halaman administratif dengan bounce rates?



#### Objective     : 
* Analisis mengenai perilaku Visitor belanja online secara in-time yang terdiri dengan memprediksi apakah Visitor tersebut menghasilkan Revenue atau tidak

* Pada program ini, kami memprediksi niat pembelian pengguna menggunakan data tampilan halaman yang dikumpulkan selama kunjungan, bersama dengan informasi sesi dan pengguna. Dengan menggunakan data ini, kami membuat model prediksi untuk memahami apakah pengunjung memiliki niat untuk melakukan pembelian atau tidak. Pada model ini digunakan metrik precision dengan tujuan meminimalisir terjadinya True Positif (pengunjung yang sebenarnya tidak belanja, namun dikategorikan belanja). Pada model ini dilakukan enam jenis model yaitu Logstic Regression, KNN, SVM, Decision Tree, Random Forest, dan XGBoost. Model XGBoost terbukti memberikan kinerja terbaik setelah dilakukan hyperparameter tuning, dengan memiliki nilai precision skor paling tinggi dibandingkan dengan model lain.

=================================================================================================================================================

HuggingFace : https://huggingface.co/spaces/raniesm/Predicting_Visitor_Conversion_on_E-Commerce_Websites
Dashboard : https://public.tableau.com/app/profile/ranie.sita/viz/FinalProject_17175110023700/Dashboard1?publish=yes
