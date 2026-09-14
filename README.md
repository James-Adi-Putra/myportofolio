Nama : James Adi Putra

NPM : 2506624644

Kelas : PBP C

Universitas Indonesia

<!-- redeploy trigger -->

### Tugas 1
1. Ya saya menggunakan elemen semantik HTML5, Section "Profile" dan "Experience" dibungkus dengan `<section>` agar tiap bagian halaman punya identitas konten yang jelas dan bisa dituju lewat navigasi link (`#profile`, `#experience`) Untuk tiap kartu pengalaman di dalam Experience, saya menggunakan `<article>` karena setiap kartu berisi konten yang berdiri sendiri dan tetap masuk akal walau dipisahkan dari kartu lain atau ditampilkan ulang di tempat berbeda. Penggunaan `<dl>`/`<dt>`/`<dd>` untuk NPM dan Program juga saya pertahankan dari Tutorial 01 karena cocok untuk data berpasangan label-nilai. Elemen-elemen ini membantu saya menjaga struktur kode mudah dimengerti dan memudahkan saya mencari bagian yang perlu diubah.
2. Ada beberapa yang perlu saya pikirkan grid dua kolom di section Profile (foto di kanan, detail di kiri) yang perlu berubah jadi satu kolom di layar sempit tanpa merusak urutan baca. Saya atasi dengan mendefinisikan ulang `grid-template-areas` di dalam media query, sehingga identity muncul dulu, lalu foto, detail urutan ini saya tentukan berdasarkan apa yang paling penting dilihat user pertama kali. Selain itu pada section Experience yang menggunakan horizontal scroll dengan `scroll-snap-type`, saya perlu memastikan lebar tiap kartu tetap nyaman disentuh/discroll di HP, sehingga saya kecilkan lebar kartu jadi 220px lewat media query supaya tidak terlalu memenuhi layar HP yang sempit tapi tetap mudah di scroll
3. Batasan paling terasa adalah semua data pengalaman harus saya tulis manual satu per satu di HTML wkwkw kalau saya ingin menambah pengalaman baru, saya harus menyalin ulang struktur `<article class="exp-card">` dan mengedit kode langsung. Untuk iterasi berikutnya, saya paling ingin menambahkan kemampuan memfilter atau mengurutkan section Experience berdasarkan kategori (misal organisasi, akademik, sosial), yang membutuhkan data disimpan di database agar bisa di query secara dinamis

### AI Disclosure Tugas 1
Saya menggunakan Claude (Anthropic) sebagai bantuan dalam beberapa bagian tugas ini, dengan rincian sebagai berikut:
1. Animasi CSS untuk bagian foto Bingkai foto dan bagian NPM serta nama
2. Membuat tampilan tombol rec berkedip disamping tulisan computer science
3. Membuat Animasi pada setiap tombol social media dengan css
**Strategi prompting:**
Saya memberi feedback spesifik setiap kali hasil AI kurang sesuai (misalnya bingkai foto yang awalnya terkesan seperti kotak scan barcode bukan kamera, warna box yang terlalu mencolok, atau efek yang terasa kurang berhasil) hingga hasilnya sesuai dengan yang saya inginkan. Saya juga aktif bertanya balik untuk memahami maksud dari kode yang diberikan (misalnya menanyakan fungsi properti tertentu) sebelum menerapkannya
**Bagian yang murni dikerjakan sendiri:**
1. Seluruh konten section Experience (5 pengalaman organisasi/kepanitiaan) ditulis berdasarkan pengalaman pribadi
2. Memikirkan brainstorming desain dari web mau dibawa ke tema seperti apa saya memutuskan tema fotografi
3. Mengambil logo social media dari simple icon
4. Mencari background yang cocok untuk background website saya di pencarian aset dan foto untuk mendapatkan aset yang saya mau
**Refleksi proses:**
Saya mengerjakan tugas 1 ini untuk melanjutkan section dari web porto saya disini saya belajar dalam penggunaan semantik di html dan membuat card experience dengan html sendiri tetap untuk bagian css memang saya masih tidak terlepas dengan bantuan AI meskipun brainstorming dan desain yang desain saya tapi implementasi tetap beberapa css saya dibantu oleh AI. Dari pengerjaan tugas ini saya sudah berhasil implementasi section experience meski mungkin ada beberapa fitur yang belum sempurna karena saya tertarik dengan pembuatan web jadi saya sebisanya untuk mencoba terlebih dahulu sendiri mengacak acak code nya. Dari tugas ini saya makin yakin PBP sepertinya akan seru untuk semester ini buat saya karena saya merasa fun untuk melakukan desain dan implementasi web dalam waktu yang lama disini.


### Tugas 2
1. Alur dimulai saat browser mengirim request ke URL `/education/`, yang diteruskan dari `portofolio/urls.py` ke `main/urls.py`hingga memanggil fungsi show_education di `main/views.py`. View ini kemudian mengambil seluruh data Education dari database, menyimpannya dalam context, dan merendernya bersama template education.html. Akhirnya, Django memproses perulangan objek di template menjadi elemen HTML utuh yang dikirimkan kembali sebagai response ke browser.
2.  Karena kemudahan pemeliharaan jadi kalau ada info yang berubah (misalnya status "Sedang berlangsung" menjadi "Selesai"), saya cukup mengubah satu baris data di database (lewat Django Admin), tanpa perlu mengedit dan mencari-cari di file HTML. Lalu konsistensi, karena data dari model dipakai lewat perulangan `{% for %}`, jumlah entri bisa bertambah atau berkurang tanpa perlu menulis ulang blok HTML baru setiap kali. Selain itu menurut saya template hanya mengatur tampilan, sedangkan model dan database mengatur isi data yang sesungguhnya, sehingga kalau nanti saya mau menambah fitur (misalnya filter atau pencarian riwayat pendidikan), ya saya tinggal menyesuaikan view dan query, tanpa perlu mengubah struktur template.
3. `makemigrations` membuat berkas migrasi baru yang mencatat perubahan yang saya buat di `models.py` tapi belum benar-benar menerapkan perubahan itu ke database. Sedangkan `migrate` adalah perintah yang benar-benar mengeksekusi berkas migrasi tersebut, sehingga struktur di database (SQLite di lokal, atau PostgreSQL di production) benar-benar berubah sesuai definisi model terbaru. Contoh nyata yang saya alami jadi waktu saya menambahkan field `description` ke model `Education` untuk menyimpan cerita singkat tiap institusi edukasi saya, saya sempat lupa menjalankan `makemigrations` dan `migrate` terlebih dahulu, sehingga muncul error `no such column: main_education.description` saat mencoba mengakses halaman Education. Setelah menjalankan kedua perintah tersebut secara berurutan, field baru itu baru benar-benar tersedia di database dan halaman bisa diakses tanpa error

## AI Disclosure
Saya menggunakan Claude (Anthropic) sebagai bantuan dalam beberapa bagian tugas ini, dengan rincian sebagai berikut:
1. Debugging error migrasi database, static files di production, dan konfigurasi environment variables
2. Bantuan menyusun struktur CSS untuk section Education, termasuk penyesuaian dari desain awal saya ke pola MVT yang diajarkan tutorial saya melemparkan sebuah desain untuk diimplementasikan code CSS nya yaitu roadmap perjalanan dan animasi munculnya
3. Bantuan penambahan CSS pada section Experience bagian card untuk membuat tampilan bersinar saat di hover kursor
4. Diskusi dan penjelasan konsep MVT, routing, migrasi model, saat saya menyesuaikan model Education dengan kebutuhan saya sendiri
**Strategi prompting:**
Saya meminta bantuan untuk desain css dari section education lalu saya melemparkan beberapa pertanyaan terkait tugas kali ini berupa konsep MVT dan migrasi serta database django admin untuk penggunaannya seperti apa. Saya juga meminta desain saya untuk divisualisasikan terlebih dahulu sebelum AI melakukan coding css section education. Terdapat beberapa bug yang terjadi sehingga aku mencoba aktif bertanya balik untuk cara mengatasi bug yang terjadi dan memberikan masukan ku untuk memperbaiki bug.
**Bagian yang murni dikerjakan sendiri:**
1. menentukan konten pribadi (bio, riwayat pendidikan, pengalaman organisasi)
2. Membuat desain mentah css bagian education lalu melempar gambar desain mentah ke AI untuk diimplementasikan
3. pengambilan keputusan desain visual dan tema yaitu merubah opasity latar belakang
4. Melakukan penyesuaian terhadap lebar kotak experience di tampilan Desktop maupun tampilan HP
5. Pengujian manual di browser dan HP menggunakan inspect untuk test performance 
