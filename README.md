link web : https://nadila-salsabila-footballcollectibles.pbp.cs.ui.ac.id/

================================ TUGAS 2 ========================================

1. Cara mengimplementasikan checklist secara step by step
   
a) Git : Inisialisasi
   
```
mkdir football-collectibles
cd football-collectibles
git init
```

b) Virtual environment dan dependencies
- Buat dan aktifkan virtual environment

```
python -m venv env
\env\Scripts\activate
```

Karena virtual environments untuk mengisolasi package serta dependencies dari aplikasi agar tidak bertabrakan dengan versi lain yang ada pada komputer

- Buat berkas requirements.txt dan install requirements.txt

`pip install -r requirements.txt`

c) Buat proyek Django dan Struktur awal

`django-admin startproject football-collectibles .`

d) Environment variables dan settings.py
- Buka file .env dan tambahkan konfigurasi 
`PRODUCTION=False`

- Buat juga file .env.prod di direktori yang sama untuk konfigurasi production

```
DB_NAME=<nama database>
DB_HOST=<host database>
DB_PORT=<port database>
DB_USER=<username database>
DB_PASSWORD=<password database>
SCHEMA=tugas_individu
PRODUCTION=True
```

Bagian ini dapat diisi dengan kredensial database yang didapatkan

- Modifikasi file settings.py untuk menggunakan environment variables

```
import os
from dotenv import load_dotenv
load_dotenv()
```

- Tambahkan string pada ALLOWED_HOSTS di settings.py 
`ALLOWED_HOSTS = ["localhost", "127.0.0.1"]`

- Tambahkan konfigurasi PRODUCTION di settings.py
`PRODUCTION = os.getenv('PRODUCTION', 'False').lower() == 'true'`

- Ubah konfigurasi database di settings.py

- Menjalankan server dan jalankan server Django

```
python manage.py migrate
python manage.py runserver
```

e) .gitignore
- Tambahkan dan isi berkas .gitignore untuk menentukan berkas-berkas dan direktori-direktori yang harus diabaikan oleh Git

f) Buat aplikasi main + register

`python manage.py startapp main`

Untuk membuat aplikasi baru dengan nama main

Kemudian, tambahkan ke settings.py di dalam direktori proyek football-collectibles

```
INSTALLED_APPS = [
    'main',
]
```

g) Membuat Product Model
- Pada main/models.py yang berisi atribut name, price, description, thumbnail, category, is_featured, stock, brand, release_year, size, edition_type, condition, authenticity_certificate, rarity_model

h) Migrasi dan run lokal

Buat migrasi

```
python manage.py makemigrations
python manage.py migrate
```

i) Implementasi Template
- Membuat direktori baru bernama templates di dalam direktori aplikasi main
- Dalam direktori templates, buat dan isi berkas main.html

j) Menghubungkan View dengan Template
- Membuka berkas views.py yang terletak di dalam berkas aplikasi main
- Tambahkan 

```
def show_main(request):
    context = {
        'nama_aplikasi' : 'Football Collectibles',
        'name': 'Nadila Salsabila Fauziyyah',
        'class': 'PBP E'
    }
    return render(request, "main.html", context)
```
- Memodifikasi template main.html

k) Mengonfigurasi Routing URL
- Buat berkas urls.py di dalam direktori main dan isi dengan kode

``` 
from django.urls import path
from main.views import show_main
app_name = 'main'
urlpatterns = [
    path('', show_main, name='show_main'),
]
```
- Mengonfigurasi Routing URL Proyek
Buat berkas urls.py di dalam direktori proyek football-collectibles, melalukan import fungsi include dari django.urls
- Menambahkan rute URL untuk mengarahkan ke tampilan main di dalam list urlpatterns

```
urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
]
```

l) Menjalankan proyek Django

`python manage.py runserver`

m) Menghentikan Server dan Menonaktifkan Virtual Environment
- Menghentikan server dengan tekan CTRL+C
- Nonaktifkan virtual environment
`deactivate`

n) Git commit dan push
```
git remote add origin <Link>
git branch -M master
git add .
git commit -m "pesan"
git push -u origin master
```

o) Melakukan deployment melalui PWS
- Akses halaman web PWS dan buat proyek baru bernama football-collectibles
- Buka tab environs, klik raw editor, dan copy paste isi file dari .env.prod
- Pada settings.py di proyek Django, tambahkan URL deployment PWS pada ALLOWED_HOSTS
- Lakukan git add, commit, dan push perubahan ke repositori GitHub
- Jalankan perintah yang terdapat pada informasi Project Command pada halaman PWS 


2. Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.oy, models.py, dan berkas html

https://drive.google.com/file/d/1UUkdu-TkOqAgvvKaMZtaCcAltZhlMz0G/view?usp=sharing

Ketika pengguna mengakses aplikasi Django melalui browser, permintaan (request) pertama kali diterima oleh urls.py, yang bertugas mencocokkan pola URL dengan rute (routing) yang sesuai. Setelah itu, Django memetakan URL tersebut ke fungsi yang ada di views.py.

File views.py berfungsi sebagai pengendali logika bisnis sekaligus penghubung antara Model dan Template untuk menentukan apa yang akan ditampilkan ke pengguna. Jika data dari database diperlukan, views.py akan berinteraksi dengan models.py, yaitu representasi struktur tabel database dalam bentuk class Python yang memungkinkan proses baca/tulis data.

Setelah data diperoleh (jika dibutuhkan), views.py akan merender Template berupa file HTML yang berisi struktur tampilan halaman (HTML, CSS, dan JavaScript) dengan data yang telah disisipkan secara terformat. Template yang sudah dirender kemudian dikembalikan ke views.py, dan akhirnya dikirimkan sebagai HTTP Response dalam bentuk halaman HTML kepada browser.

Dengan demikian, alur MVT secara sederhana dapat digambarkan sebagai:
Request → urls.py → views.py → models.py → views.py → Template → Response


3. Jelaskan peran settings.py dalam proyek Django

File setting.py adalah pusat konfigurasi dalam proyek Django yang berisi berbagai pengaturan yang mengontrol jalannya aplikasi web.

Fungsi Utama settings.py : 
- Konfigurasi Aplikasi

Melalui variabel INSTALLED_APPS, developer mendaftarkan aplikasi yang digunakan dalam proyek. Tanpa mendaftarkannya di sini, aplikasi tidak dapat dijalankan oleh Django.
- Pengaturan Basis Data

settings.py menyimpan detail konfigurasi koneksi ke database (nama database, user, password, host, port, dan engine yang digunakan).
- Internasionalisasi dan Lokalisasi

Menyediakan pengaturan bahasa, zona waktu, serta format tanggal dan angka sesuai kebutuhan pengguna.

Dengan kata lain, settings.py adalah pusat kendali proyek Django yang memastikan semua komponen aplikasi dapat berjalan sesuai konfigurasi yang diinginkan


4. Bagaimana cara kerja migrasi database di Django

Migrasi database (Data Migration) di Django adalah mekanisme untuk memperbarui struktur basis data (schema) agar tetap konsisten dengan perubahan pada model aplikasi. Proses ini memudahkan developer dalam menambahkan, mengubah, atau menghapus tabel dan field tanpa harus menulis query SQL manual.

Migrasi model adalah cara Django melacak perubahan pada model basis data. Migrasi ini berisi instruksi untuk mengubah struktur tabel basis data sesuai dengan perubahan model yang didefinisikan dalam kode terbaru.

Cara Kerja Migrasi
- Perubahan Model

Developer melakukan perubahan di file models.py, misalnya menambahkan field baru atau membuat model baru
- Membuat File Migrasi

`python manage.py makemigrations`

Django akan membuat file migrasi yang berisi instruksi perubahan berdasarkan model terbaru.
- Menerapkan Migrasi

`python manage.py migrate`

Perintah ini akan mengeksekusi perubahan pada database sesuai file migrasi yang dibuat.

Kapan Migrasi Data Digunakan
- Pengaturan data awal : Mengisi tabel dengan data default
- Nilai default : Memberikan nilai pada field baru yang non-nullable
- Transformasi data : Mengubah format data agar sesuai dengan kebutuhan baru
- Pembersihan data : Menghapus atau memperbaiki data yang inkonsisten

5. Mengapa framerok Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django merupakan salah satu framework Python yang sangat populer, bersifat skalabel, aman, dan dilengkapi banyak fitur bawaan, sehingga menjadi pilihan tepat bagi pemula yang ingin belajar pengembangan perangkat lunak. Beberapa alasan utamanya adalah:
- Mudah Dipelajari dan Cepat Dikembangkan

Django dirancang agar developer bisa membangun website dengan cepat tanpa banyak kesulitan. Jika sudah menguasai dasar Python dan konsep website, maka memulai dengan Django relatif mudah. Dokumentasi yang lengkap serta banyaknya tutorial menjadikan kurva belajarnya ramah untuk pemula.
- Kecepatan Pengembangan

Django memiliki arsitektur terorganisasi dengan baik. Framework ini memungkinkan pengembang untuk segera menerapkan arsitektur web ke dalam kode dengan cepat, mendukung rapid development dan desain yang bersih serta pragmatis.
- Hemat Biaya dan Open Source

Django adalah framework gratis dan open-source, dengan komunitas aktif yang terus mengembangkan dan memelihara proyek ini. Dukungan juga diberikan oleh Django Software Foundation, sehingga pemeliharaannya terjamin.
- Fitur Lengkap dan Fleksibel

Django menyediakan banyak library, API, dan modul bawaan. Dengan prinsip “Don’t Repeat Yourself (DRY)”, developer tidak perlu menulis kode berulang kali. Selain itu, Django juga fleksibel, bisa digunakan untuk proyek kecil maupun aplikasi skala besar, dari sekadar blog sederhana hingga sistem enterprise.
- Menyederhanakan Proses Development

Django sudah menyediakan berbagai tools bawaan yang bisa langsung digunakan, misalnya untuk autentikasi, manajemen user, dan admin panel. Selain itu, ada juga banyak package tambahan yang dapat mendukung kebutuhan modern seperti analisis data, AI, dan machine learning.
- Object-Relational Mapping yang Kuat

Django memiliki ORM bawaan yang powerful sehingga developer tidak perlu menulis query SQL secara manual untuk mengakses database. Hal ini mempermudah interaksi dengan database sekaligus membuat kode lebih ringkas dan aman.

6. Feedback untuk asisten dosen tutorial 1 yang telah dikerjakan sebelumnya?

Banyak bagian yang sudah dijelaskan dengan baik, namun ada beberapa bagian yang masih membingungkan. Misalnya, ketika terdapat instruksi untuk membuka suatu file, belum ada kejelasan mengenai file di folder mana yang dimaksud.


Daftar Referensi 

AWS. (n.d.). Apa itu Django? AWS. https://www.aws.amazon.com/id/what-is/django/

Bagus, A. S. (2018, Februari 3). Cara membuat data migration dengan Django. CodePolitan. https://www.codepolitan.com/blog/cara-membuat-data-migration-dengan-django-5a749614988e4/

Biznet. (2023, April 12). Django, framework Python untuk mempermudah kustomisasi website. BiznetGio. https://www.biznetgio.com/news/django

Boluwatife, F. (2023, April 7). How to get up and running with Django migrations: A guide. CoderPad. https://coderpad.io/blog/development/how-to-get-up-and-running-with-django-migrations-a-guide/

CodePolitan. (2018, Februari 2). Cara membuat data migration dengan Django. Diakses dari https://www.codepolitan.com/blog/cara-membuat-data-migration-dengan-django-5a749614988e4/

Django Project. (n.d.). Menulis aplikasi pertama Anda, Bagian 1. Dalam Dokumentasi Django 4.1. Diakses dari https://docs.djangoproject.com/id/4.1/intro/tutorial01/

Fernando, V. K., Grady, C., Scafi, M., & Danniel. (2025, Agustus 21). Tutorial 1: Pengenalan aplikasi Django dan Model-View-Template (MVT) pada Django. PBP Fasilkom UI. https://pbp-fasilkom-ui.github.io/ganjil-2026/docs/tutorial-1

Jagoan Hosting Team. (2024, Agustus 10). Mengenal Django, web framework dengan banyak kelebihan. Jagoan Hosting. https://www.jagoanhosting.com/blog/django/

Kramer, N. (2024, April 17). Django for beginners: An introduction. daily.dev. https://daily.dev/blog/django-for-beginners-an-introduction

Marlena, M., & Buana, I. C. (2025, Agustus 27). Tutorial 0: Konfigurasi dan instalasi Git dan Django. PBP Fasilkom UI. https://pbp-fasilkom-ui.github.io/ganjil-2026/docs/tutorial-0

Polin, Y. (2020, Desember 22). Settings and URLs Django. Medium. Diakses dari https://yohanapolin.medium.com/settings-and-urls-django-f55acd925b23

Python Plain English. (2023, September 10). Understanding Setting.py in Your Django Project. Diakses dari https://python.plainenglish.io/setting-py-a-quick-guide-to-your-django-project-e3aa0bbcdb34

VinDevs. (2024, Oktober 9). How to write a Django data migration: How they work. VinDevs. https://vindevs.com/blog/how-to-write-a-django-data-migration-how-they-work-p76/


================================ TUGAS 3 ========================================

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Dalam pengimplementasian sebuah platform, data delivery memiliki peranan penting karena memungkinkan pertukaran data antar stack atau sistem secara aman, efisien, dan fleksibel. Data yang dikirimkan dapat berbentuk beragam format seperti HTML, XML, maupun JSON.

Data delivery tidak hanya berfokus pada pemindahan data, tetapi juga mencakup orchestrasi akses, kontrol keamanan, penjadwalan, format penyesuaian, serta kepatuhan terhadap regulasi. Dengan demikian, proses pengiriman data dapat dilakukan dengan cara yang transparan, ramah pengguna, sekaligus hemat biaya operasional.

Dari perspektif bisnis, data delivery adalah tahapan akhir dari perjalanan data: ketika hasil pengumpulan, pengolahan, dan analisis data benar-benar sampai ke pengguna akhir. Jika proses ini terlambat, tidak konsisten, atau terlalu mahal, maka dapat menurunkan kepercayaan serta kepuasan pengguna. Sebaliknya, data delivery yang tepat waktu dan aman meningkatkan loyalitas pengguna serta mengurangi risiko kebocoran data.

Dengan demikian, data delivery menjadi aspek krusial dalam pengimplementasian platform modern, baik dari sisi teknis (efisiensi, integrasi, keamanan) maupun bisnis (kepuasan, kepercayaan, loyalitas pengguna).

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

XML (eXtensible Markup Language) dan JSON (JavaScript Object Notation) sama-sama digunakan sebagai format pertukaran data antar aplikasi. XML memiliki keunggulan dalam menangani data kompleks, mendukung validasi dengan schema yang ketat, serta telah lama menjadi standar internasional yang kompatibel dengan banyak sistem lama. XML juga cocok digunakan dalam pembuatan dokumentasi teknis dan transformasi data lintas format menggunakan XSLT.

Namun, XML memiliki beberapa kelemahan, seperti sintaks yang verbose dan memerlukan parser khusus untuk memproses data. Hal ini mendorong pengembangan JSON sebagai alternatif yang lebih ringan, sederhana, dan efisien. JSON menggunakan struktur key-value pairs dengan sintaks yang ringkas, mudah dibaca, serta dapat diurai langsung oleh JavaScript tanpa parser tambahan. JSON juga mendukung penggunaan database dokumen (document databases) yang fleksibel dan mudah diperbarui.

Meski lebih populer, JSON juga memiliki beberapa kelemahan:
- JSON tidak dapat merepresentasikan struktur data yang serumit XML, sehingga dalam aplikasi enterprise dengan arsitektur dan kompleksitas berbeda, hal ini dapat menimbulkan kesalahan di lapisan aplikasi yang lebih tinggi.

- JSON berpotensi mengandung risiko keamanan serius, di mana aktor jahat dapat menyisipkan kode JavaScript berbahaya ke dalam string. Jika ada kode JavaScript lain di pernyataan sebelumnya, browser dapat mengeksekusi kode berbahaya tersebut, berpotensi memberikan akses ke komputer pengguna.

Google Trends menunjukkan bahwa minat pencarian terhadap JSON telah melampaui XML sejak 2015, menandakan pergeseran signifikan di kalangan pengembang.

Pemilihan antara JSON dan XML sangat bergantung pada kebutuhan spesifik proyek. JSON umumnya lebih disukai untuk aplikasi web karena formatnya yang ringan, deskriptif, mudah dibaca, dan kompatibel dengan kerangka kerja JavaScript, serta mendukung penguraian yang cepat. Sebaliknya, XML lebih cocok untuk aplikasi yang membutuhkan representasi data yang kompleks dan validasi mendalam. XML juga menawarkan deskripsi yang lebih rinci dan berbagai fitur tambahan.

Secara umum, JSON lebih populer dibandingkan XML karena formatnya yang lebih ringan, sederhana, mudah dipahami, dan cocok untuk kebutuhan aplikasi modern. Sementara itu, XML tetap relevan dalam konteks tertentu, terutama untuk sistem lama dan aplikasi yang memerlukan representasi data kompleks serta validasi mendalam.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Dalam Django, method is_valid() pada objek form berfungsi untuk melakukan validasi data yang telah di-bind ke form. Dengan memanggil method ini, Django akan menjalankan seluruh prosedur validasi, termasuk pengecekan tipe data Python, aturan validasi tiap field, serta validasi di tingkat form. Method ini kemudian mengembalikan nilai boolean:
- True apabila semua data valid,
- False apabila terdapat satu atau lebih kesalahan.

Jika is_valid() mengembalikan True, maka data yang sudah tervalidasi dan dibersihkan dapat diakses melalui atribut form.cleaned_data. Data ini telah otomatis dikonversi ke tipe Python yang sesuai, sehingga memudahkan proses lanjutan seperti penyimpanan ke database atau penggunaan dalam logika aplikasi.

Kita membutuhkan is_valid() karena:
- Menjamin keakuratan dan keamanan data : Hanya data yang sesuai aturan validasi yang akan diproses lebih lanjut.
- Mengubah data menjadi tipe Python yang sesuai : Memudahkan penggunaan data dalam kode.
- Menyediakan umpan balik error : Jika validasi gagal, detail kesalahan dapat diakses melalui atribut errors, sehingga aplikasi dapat menampilkan pesan yang membantu pengguna memperbaiki input.

Dengan demikian, is_valid() merupakan komponen inti dalam mekanisme form Django yang memastikan data yang masuk ke aplikasi valid, aman, dan siap dipakai.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Dalam Django, csrf_token diperlukan untuk melindungi aplikasi web dari serangan Cross-Site Request Forgery (CSRF). CSRF adalah jenis serangan di mana penyerang memanfaatkan sesi pengguna yang sedang aktif (authenticated) untuk melakukan aksi berbahaya tanpa sepengetahuan korban. Misalnya, pengguna bisa diarahkan melalui link, form palsu, atau skrip berbahaya untuk melakukan aksi seperti mengubah email, transfer dana, atau manipulasi data lain.

Saat sesi pengguna dimulai, Django secara otomatis menghasilkan token CSRF yang unik, rahasia, dan tidak dapat diprediksi. Token ini disertakan dalam setiap form POST melalui tag {% csrf_token %} di template. Ketika form dikirim, server akan membandingkan token pada request dengan token yang tersimpan di sesi pengguna. Jika token hilang atau tidak cocok, permintaan akan ditolak karena dianggap tidak valid.

Jika form Django tidak menggunakan csrf_token, aplikasi menjadi rentan terhadap serangan CSRF. Penyerang bisa:
- Mengirimkan permintaan berbahaya dengan memanfaatkan kredensial pengguna yang masih login.
- Melakukan aksi sensitif tanpa persetujuan pengguna, misalnya transaksi keuangan atau perubahan data akun.
- Bahkan, dalam kasus login CSRF, penyerang dapat memaksa browser korban untuk login dengan kredensial penyerang, sehingga korban tanpa sadar melakukan aktivitas dengan akun palsu.

Dengan demikian, penggunaan csrf_token sangat penting untuk menjamin keaslian request yang dikirimkan oleh pengguna, melindungi data, dan menjaga keamanan aplikasi web.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

a) Buat direktori templates pada direktori utama dan buat berkas `base.html`

b) Buka `settings.py` pada direktori proyek dan sesuaikan kode pada variabel `TEMPLATES` 

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan konten baris ini
        'APP_DIRS': True,
        ...
    }
]
```

c) Pada `main/templates/`, ubah kode berkas `main.html` 

d) Buat berkas baru pada direktori main dengan nama `forms.py`. Tambahkan kode pada `forms.py`

e) Buka berkas `views.py` yang ada pada direktori main dan tambahkan beberapa import pada bagian paling atas, kemudian perbarui dan tambahkan fungsi-fungsi.

f) Buka `urls.py` yang ada pada direktori main dan import fungsi-fungsi yang sudah dibuat, kemudian tambahkan path URL ke dalam variabel urlpatterns

g) Buka `main.html` pada direktori `main/templates` dan update kode di dalam blok `content`

h) Buat dua berkas HTML baru pada direktori `main/templates` untuk halaman form input dan detail produk : `create_product.html` dan `product_detail.html`

i) Buka `settings.py` pada direktori root project dan tambahkan entri url proyek pws pada `CSRF_TRUSTED_ORIGINS` tepat setelah `ALLOWED_HOSTS`

j) Jalankan perintah Django dengan perintah `python manage.py runserver`

k) Buka `views.py` pada direktori main dan tambahkan import pada bagian paling atas. Buat fungsi baru yang menerima parameter request dengan nama show_xml dan buat sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari seluruh data yang ada pada Product. Tambahkan return function berupa `HttpResponse` yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML dan parameter `content_type="application/xml"`

l) Buka `views.py` pada direktori main dan tambahkan import pada bagian paling atas. Buat fungsi baru yang menerima parameter request dengan nama show_json dan buat sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari seluruh data yang ada pada Product. Tambahkan return function berupa `HttpResponse` yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON dan parameter `content_type="application/json"`

m) Buka `views.py` pada direktori main dan buat fungsi yang menerima parameter request dan product_id dengan nama `show_xml_by_id` dan `show_json_by_id`. Buat variabel di dalam fungsi tersebut yang menyimpan hasil query dari data dengan id tertentu. Tambahkan return function berupa `HttpResponse` yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON atau XML dan parameter content_type dengan value `”application/xml”` atau `”application/json”`. Tambahkan blok try except pada fungsi untuk mengantisipasi kondisi ketika product_id tertentu tidak ditemukan dalam  basis data. Jika data tidak ditemukan, kembalikan `HttpResponse` dengan status 404 sebagai tanda data tidak ada.

n) Buka `urls.py` pada direktori main dan import fungsi yang sudah dibuat

o) Tambahkan path url ke dalam urlpatterns untuk akses fungsi yang sudah diimpor

p) Buka Postman dan buat request baru dengan method `GET` dan url http://localhost:8000/xml/ atau http://localhost:8000/json/ untuk mengetes apakah data terkirimkan dengan baik. Kemudian, klik tombol `Send` untuk mengirimkan request tersebut.

q) Ubah url menjadi  http://localhost:8000/xml/[news_id] atau http://localhost:8000/json/[news_id] untuk mengetes fungsi pengambilan data News berdasarkan ID.

r) Lakukan Git Commit dan Push

```
git add .
git commit -m "pesan"
git push -u origin master
git push pws master
```

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?

Terdapat beberapa kendala ketika menggunakan Postman, khususnya saat mengetes fungsi pengambilan data newsberdasarkan ID. Saya sempat kebingungan karena tidak tahu di bagian mana ID tersebut dapat dilihat. Selain itu, ada beberapa potongan kode yang belum dijelaskan secara detail, sehingga menimbulkan sedikit kebingungan dalam memahami alurnya.

7. Screenshot hasil akses URL pada Postman

Postman JSON : https://drive.google.com/file/d/1EkEn34TzufMLcrq77Gl7cWr7aJdqk9JO/view?usp=sharing

Postman XML : https://drive.google.com/file/d/1mOoRCYRU3oDD410P8vxe_1tXdRikyz4D/view?usp=sharing

Postman JSON berdasarkan ID : https://drive.google.com/file/d/1GQcJGJ9_F3VEV29eoOmJ6lZTFtrmn0hI/view?usp=sharing

Postman XML berdasarkan ID : https://drive.google.com/file/d/1KVvK6Ix3zjbTTJHoGPaxtU-dg09KHSld/view?usp=sharing

Daftar Referensi

Fiona Ratu Maheswari (FIO), Anthony Edbert Feriyanto (ANT), Meutia Fajriyah (MEW), & Yeshua Marco Gracia (ACO). (2025, Agustus 27). Tutorial 2: Form dan Data Delivery. PBP Fasilkom UI. Retrieved from https://pbp-fasilkom-ui.github.io/ganjil-2026/docs/tutorial-2

Monda. (n.d.). What is a Data Delivery? Retrieved from https://www.monda.ai/glossary/data-delivery

Monda. (2025). The State of Data Delivery 2025. Retrieved from https://www.monda.ai/reports/state-of-data-delivery-2025

Coursera Staff. (2025, July 4). JSON vs. XML: What’s The Difference? Retrieved from https://www.coursera.org/articles/json-vs-xml

Google Trends. (n.d.). Membandingkan JSON dan XML. Retrieved from https://trends.google.com/trends/explore?date=all&geo=US&q=json,xml

Ultahost. (2024, Agustus 30). Perbandingan antara XML dan JSON, Mana yang Lebih Baik? Retrieved from https://ultahost.com/blog/id/perbandingan-antara-xml-dan-json-mana-yang-lebih-baik/

Django. (n.d.). Form and field API reference. In Django documentation (version 5.2). Retrieved from https://docs.djangoproject.com/en/5.2/ref/forms/api/

Django documentation. (n.d.). Working with forms. Retrieved from https://django.readthedocs.io/en/latest/topics/forms/

Django. (n.d.). Cross Site Request Forgery protection. In Django documentation (version 5.2). Retrieved from https://docs.djangoproject.com/en/5.2/ref/csrf/

GeeksforGeeks. (2025, August 5). CSRF token in Django. Retrieved from https://www.geeksforgeeks.org/python/csrf-token-in-django/

Dizdar, A. (2021, June 11; modified 2025, March 25). What is a CSRF Token and How Does It Work? Brightsec. Retrieved from https://brightsec.com/blog/csrf-token/


================================ TUGAS 4 ========================================

1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

AuthenticationForm adalah form bawaan di Django (`modul django.contrib.auth.forms`) yang digunakan untuk menangani proses login (autentikasi) user. Form ini memeriksa username, password, serta flag is_active, dan Django juga memudahkan penambahan verifikasi kustom.

#### Kelebihan
- Sudah banyak diuji oleh berbagai aplikasi yang menggunakannya di production.
- Dukungan resmi (first-party support) karena bagian dari ekosistem Django.
- Fleksibel, dibangun secara generik sehingga mudah diperluas sesuai kebutuhan.
- Sederhana dan mudah dipahami.

#### Kekurangan
- Ada learning curve dan pengetahuan ini tidak langsung bisa diterapkan ke sistem autentikasi lain
- Karena dibuat generik, diharapkan untuk dikustomisasi agar sesuai dengan kebutuhan, yang bisa menjadi merepotkan.
- Sistem autentikasi sederhana yang mungkin tidak cocok untuk aplikasi dengan kebutuhan kompleks.
- Tidak mendukung advanced use cases secara default sehingga developer perlu membangun dan merawat banyak logika kustom.

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

Authentication (AuthN) adalah proses verifikasi identitas seseorang atau suatu layanan, memastikan bahwa mereka adalah siapa yang mereka klaim. Contoh: ketika login ke sebuah situs, user memasukkan username dan password, lalu sistem mencocokkannya dengan data di database. Jika cocok, sistem menganggap user valid.

Authorization (AuthZ) adalah proses keamanan untuk menentukan tingkat akses user atau layanan, yaitu apakah mereka berhak mengakses data tertentu atau melakukan suatu aksi.

Autentikasi selalu dilakukan sebelum otorisasi, karena sistem tidak bisa memberikan izin tanpa mengetahui siapa user tersebut.

#### Implementasi di Django
Django menggunakan model `User` (atau custom user model) untuk merepresentasikan pengguna.

a) Autentikasi
- register : user membuat akun baru, lalu data User tersimpan di database.
- login_user : memanggil authenticate() untuk cek username dan password. Jika valid, login() dipanggil, Django menyimpan session, dan request.user otomatis terisi.
- logout_user : menghapus session user, sehingga request.user kembali menjadi AnonymousUser.

Contoh : 
```
{% if product.user %}
    <p>Seller: {{ product.user.username }}</p>
{% else %}
    <p>Seller: Anonymous</p>
{% endif %}
```

b) Otorisasi
- @login_required(login_url='/login') : hanya user yang sudah login boleh mengakses view tertentu. Jika belum login, user akan diarahkan ke halaman login.
- Product.objects.filter(user=request.user) : membatasi data yang bisa diakses, misalnya user hanya bisa melihat produk miliknya sendiri.

Contoh : 
```
@login_required(login_url='/login')
def show_main(request):
    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)
```

3.  Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

Session (sesi) adalah cara bagi situs web untuk menyimpan data pengguna sementara selama pengguna masih aktif di situs tersebut. Data disimpan di server, dan biasanya hilang setelah pengguna menutup browser atau setelah periode tertentu tanpa aktivitas.

#### Kelebihan Session 
- Data tersimpan di server sehingga lebih aman.
- Cocok untuk data sensitif seperti status login.
- Otomatis terhapus setelah tidak aktif.

#### Kekurangan Session
- Membebani server karena harus menyimpan banyak data.
- Tidak bisa bertahan lama setelah browser ditutup (kecuali diatur khusus).


Cookie adalah file kecil yang disimpan di perangkat pengguna oleh browser. Cookie menyimpan data di sisi klien (browser), misalnya preferensi bahasa, produk yang pernah dilihat, atau data login. Tidak seperti session, cookie bisa tetap ada meskipun browser ditutup.

#### Kelebihan Cookie
- Bisa menyimpan data untuk jangka panjang
- Cocok untuk menyimpan preferensi pengguna
- Tidak membebani server karena data disimpan di browser
#### Kekurangan Cookie
- Kurang aman jika digunakan untuk menyimpan data sensitif
- Bisa dihapus oleh pengguna kapan saja
- Ukuran data terbatas


4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

Penggunaan cookies tidak otomatis aman secara default. Django memang sudah menyediakan dasar yang baik, tetapi tidak berarti sempurna di semua lingkungan. Developer tetap harus memastikan pengaturan keamanan ditetapkan dengan benar.

#### Risiko Potensial pada Cookies
a) Pembajakan Sesi
- Penyerang dapat mencegat cookie yang dikirimkan melalui jaringan tidak aman (misalnya Wi-Fi publik) dengan teknik packet sniffing
- Jika cookie berhasil ditangkap, penyerang bisa memperoleh session identifier dan menyamar sebagai pengguna tanpa perlu mengetahui kredensial

b) Cross-Site Scripting (XSS)
- Terjadi jika penyerang menyuntikkan kode berbahaya ke situs
- Jika input tidak divalidasi dengan benar, skrip berbahaya dapat mencuri cookie pengguna

c) Cross-Site Request Forgery (CSRF)
- Penyerang mengelabui pengguna agar tanpa sadar melakukan aksi di situs web
- Browser mengirimkan cookie autentikasi, sehingga penyerang bisa memanfaatkan sesi pengguna untuk melakukan tindakan berbahaya

#### Cara Django Menangani Risiko Ini
a) Pengaturan Cookie yang Aman
- SESSION_COOKIE_HTTPONLY = True :  mencegah cookie diakses oleh JavaScript (mengurangi risiko XSS)
- SESSION_COOKIE_SECURE = True :  memastikan cookie hanya dikirim lewat koneksi HTTPS
- CSRF_COOKIE_SECURE dan CSRF_COOKIE_HTTPONLY juga bisa diaktifkan untuk perlindungan tambahan

b) Manajemen Sesi
- Django mendukung penggunaan pengidentifikasi sesi yang kuat, waktu kedaluwarsa sesi, dan penghapusan sesi setelah logout
- Developer bisa menambahkan autentikasi dua faktor untuk keamanan ekstra

c) Validasi Input dan Penyandian Output
- Input pengguna harus divalidasi dan dibersihkan
- Karakter berbahaya difilter atau dienkode sebelum ditampilkan untuk mencegah eksekusi skrip (XSS)

d) Perlindungan CSRF
- Django secara default menyertakan CSRF token pada setiap form
- Token ini diverifikasi di sisi server untuk memastikan permintaan sah, bukan hasil pemalsuan


5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

a) Membuat Fungsi dan Form Registrasi
- Buka `views.py` pada subdirektori main. 
- Tambahkan import `UserCreationForm` dan `messages` untuk memudahkan pembuatan formulir pendaftaran pengguna dalam aplikasi web. Dengan formulir ini, pengguna dapat mendaftar dengan mudah di situs web tanpa harus menulis kode dari awal
- Tambahkan fungsi `register` di dalam `views.py`. Fungsi ini akan menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form
- Buat dan isi berkas HTML baru dengan nama `register.html` pada direktori `main/templates`
- Buka `urls.py` pada subdirektori `main` dan impor fungsi `register`
- Tambahkan path url ke dalam `urlpatterns` untuk mengakses fungsi `register`

b) Membuat Fungsi Login
- Buka `views.py` pada subdirektori `main`. Tambahkan import `authenticate`, `login`, dan `AuthenticationForm` untuk melakukan autentikasi dan login (jika autentikasi berhasil)
- Tambahkan fungsi `login_user` di dalam `views.py` untuk mengatutensikasi pengguna yang ingin login
- Buat dan isi berkas HTML baru dengan nama `login.html` pada direktori `main/templates`
- Buka `urls.py` pada subdirektori `main` dan import fungsi `login_user`
- Tambahkan path url ke dalam `urlpatterns` untuk mengakses fungsi `login_user`

c) Membuat Fungsi Logout
- Buka `views.py` pada subdirektori `main`. Tambahkan import `logout`, `authenticate`, dan `login`
- Tambahkan fungsi `logout_user` di dalam `views.py` untuk melakukan mekanisme logout
- Buka berkas `main.html` pada direktori `main/templates` dan tambahkan kode di bawah ini

```
<a href="{% url 'main:logout' %}">
 <button>Logout</button>
</a>
```

- Buka `urls.py` pada subdirektori `main` dan import fungsi `logout_user`
- Tambahkan path url ke dalam `urlpatterns` untuk mengakses fungsi `logout_user`

d) Merestriksi Akses Halaman Main dan Products Detail
-  Buka `urls.py` pada subdirektori `main` dan import fungsi `logout_user`
- Tambahkan path url ke dalam `urlpatterns` untuk mengakses fungsi `logout_user`

e) Menggunakan Data dari Cookie
- Buka `views.py` di subdirektori `main`. Tambahkan import `HttpResponseRedirect`, `reverse`, dan `datetime`
- Ubah bagian kode di fungsi `login_user` untuk menyimpan cookie baru bernama `last_login` yang berisi timestamp terakhir kali pengguna melakukan login

```
if form.is_valid():
   user = form.get_user()
   login(request, user)
   response = HttpResponseRedirect(reverse("main:show_main"))
   response.set_cookie('last_login', str(datetime.datetime.now()))
   return response
```

- Pada fungsi `show_main`, tambahkan potongan kode 
`'last_login': request.COOKIES['last_login']`
ke dalam variabel `context`
- Ubah fungsi `logout_user` untuk menghapus cookie last_login setelah melakukan logout.
- Buka berkas `main.html` di direktori `main/templates` dan tambahkan kode untuk menampilkan data waktu terakhir pengguna login.

f) Menghubungkan Model Product dengan User
- Buka `models.py` pada subdirektori `main`, kemudian import `User`
- Pada model `Product`, tambahkan 
`user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)`
- Buat file migrasi model dengan 
`python manage.py makemigrations`. Selanjutnya jalankan migrasi model dengan
`python manage.py migrate`
- Buka `views.py` pada subdirektori `main` dan ubah kode pada fungsi `create_product`
- Modifikasi fungsi `show_main`
- Tambahkan tombol filter My dan All pada halaman `main.html`
- Tampilkan nama seller di `product_detail.html`
- Jalankan proyek Django dengan perintah
`python manage.py runserver`

g) Lakukan add, commit, push ke GitHub dan PWS
```
git add .
git commit -m "<pesan_commit>"
git push origin master
git push pws master
```


### Daftar Referensi

Freitas, V. (2016, August 12). Django tips #10: AuthenticationForm custom login policy. Simple is Better Than Complex. https://simpleisbetterthancomplex.com/tips/2016/08/12/django-tip-10-authentication-form-custom-login-policy.html

Shah, N. (2024, November 18). A comprehensive guide to Django's user authentication system. SuperTokens. https://supertokens.com/blog/django-user-authentication

OneLogin. (n.d.). Authentication vs. authorization. OneLogin. https://www.onelogin.com/learn/authentication-vs-authorization

Marlena, M., Raihandrawan, F. Z., Akhdan, E., Thang, N., Alkindi, M. M., & Karina, G. (2026). Tutorial 3: Autentikasi, session, cookies dan Selenium. PBP Fasilkom UI. https://pbp-fasilkom-ui.github.io/ganjil-2026/docs/tutorial-3

Skemadigital. (2025, July 13). Pengertian session dan cookie. Skemadigital. https://skemadigital.id/blog/pengertian-session-dan-cookie/

Django Software Foundation. (n.d.). Django settings. Django documentation (Version 5.2). https://docs.djangoproject.com/en/5.2/ref/settings/

EITCA Academy. (2023, August 4). Apa risiko keamanan yang terkait dengan cookie dan bagaimana cookie dapat dieksploitasi oleh penyerang untuk menyamar sebagai pengguna dan mendapatkan akses tidak sah ke akun? EITCA. https://id.eitca.org/cybersecurity/eitc-is-acss-advanced-computer-systems-security/network-security/web-security-model/examination-review-web-security-model/what-are-the-security-risks-associated-with-cookies-and-how-can-they-be-exploited-by-attackers-to-impersonate-users-and-gain-unauthorized-access-to-accounts/