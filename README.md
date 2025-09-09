link web : https://nadila-salsabila-footballcollectibles.pbp.cs.ui.ac.id/

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