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


## Tugas 3
1. Karena field-nya otomatis di generate sesuai model yang udah saya definisikan di `models.py`. Jadi saya nggak perlu nulis satu-satu `<input>` buat tiap field, dan Django juga otomatis validasi tipe datanya misalnya field `URLField` bakal otomatis ditolak kalau isinya bukan link yang valid. Ini juga yang bikin saya bisa pakai form yang sama buat Create dan Update sekaligus, tinggal kasih parameter `instance=` waktu mau edit data yang udah ada, jadi nggak perlu bikin dua form terpisah.
Soal `{% csrf_token %}`, itu wajib karena tanpa token ini form rawan kena serangan CSRF situs lain bisa aja bikin form palsu yang diam-diam ngirim request (misalnya hapus data) ke website pas lagi login, tanpa saya sadar. Token ini kayak "kode rahasia" yang Django kasih ke tiap form, dan Django cuma bakal proses submit kalau tokennya cocok. 
2. Menurut saya JSON lebih enak dipakai karena strukturnya lebih ringkas dibanding XML nggak perlu nulis closing tag kayak `</tag>` di tiap elemen lebih ringkas juga sih
3. Waktu endpoint `/api/education/` diakses, view `get_education_json` mengambil data lewat `Education.objects.all()`, lalu `serializers.serialize("json", ...)` mengubah objek Django itu jadi string JSON sebelum dikirim lewat `HttpResponse`. Serialization diperlukan karena objek Model Django adalah struktur data internal Python yang nggak bisa langsung dipahami sistem lain, jadi harus diterjemahkan dulu ke format teks universal. `show_education` juga sengaja mengambil datanya lewat proses serialize-deserialize ini, bukan langsung query database, supaya polanya sama seperti data yang datang dari API terpisah

## Strategi Prompting
Aku menggunakan pendekatan step-by-step: meminta satu langkah dulu, mencoba menjalankannya sendiri, baru meminta lanjutan atau bantuan debug kalau menemukan error
## AI Disclosure
Saya menggunakan Claude (Anthropic) sebagai bantuan dalam beberapa bagian tugas ini, dengan rincian sebagai berikut:
1. Panduan step-by-step membangun fitur CRUD (Create, Update, Delete) termasuk penjelasan cara `instance=` dipakai supaya form yang sama bisa dipakai untuk Create dan Update
2. Implementasi endpoint JSON (`get_education_json`) dan penyesuaian `show_education` supaya mengambil data lewat proses serialize-deserialize, mengikuti pola yang sama seperti Project di Tutorial 03
3. Refactor modal konfirmasi hapus jadi satu component reusable (`confirm_delete.html`) yang dipakai bersama untuk Project dan Education, supaya tidak ada duplikasi kode
4. Perbaikan dan debug beberapa kode css yang terlalu menumpuk dan tidak efisien secara fungsi bisa disederhanakan
## Bagian yang saya kerjakan sendiri : 
1. Keputusan menambahkan field `logo` sebagai URL (bukan file lokal) untuk konsistensi dengan Project, termasuk mencari solusi sendiri saat Google Drive menghilangkan transparansi gambar dan akhirnya memilih GitHub raw URL
2. Semua kode aku ketik dan jalankan sendiri, dicek langsung di browser (lokal dan production) sebelum lanjut
3. Debug awal mandiri sebelum minta bantuan AI, seperti waktu menemukan ada fungsi `delete_project` yang terduplikasi di `views.py` sehingga password check tidak berjalan
## Refleksi Proses
Selama proses ini saya jadi tau bagaimana cara kerja django admin dengan membuat sistem CRUD sendiri sebelum ini saya memasukkan data secara manual menggunakan superuser di django admin tanpa tau cara build dari nol. Dengan bantuan AI untuk melakukan refactor pada struktur CSS tentunya karena ada beberapa code CSS yang redundan dan perlu disederhanakan next akan melanjutkan tutorial 4 dulu sambil memperbaiki beberapa tampilan notifikasi dan css lain yang masih mau diubah.


## Tugas 4
1. 
## Strategi Prompting
Saya menanyakan hal yang menurut saya perlu diklarifikasi seperti bagian sensitif di json itu apa saja, lalu saya meminta AI untuk mencatat checkpoint yang sudah saya kerjakan 
## AI Disclosure
Saya menggunakan Claude (Anthropic) dan Deepseak sebagai bantuan dalam beberapa bagian tugas ini, dengan rincian sebagai berikut:
1. Menjelaskan konsep otorisasi, CSRF, dan ManyToMany.
2. Meninjau kebocoran data di endpoint JSON 
3. Merapikan dan mengorganisasi ulang CSS, serta usulan desain kotak NPM dan Program.
4. Membuat palete warna CSS dan mengelompokkan shadow di bagian root agar tidak hardcode langsung di code lagi
5. Membantuku aku dalam membagi dan menjelaskan perah superUser, Editor, dan User biasa
## Bagian yang saya kerjakan sendiri : 
1. Mencari bug yang masih terdapat pada website ku yaitu bug EndPoint JSON dan bug CSS
2. Melakukan desain CSS dengan merubah warna desain yang awalnya dominan putih merah menjadi dominan putih gold agar lebih cerah dan terlihat di background hitam
3. Melakukan perubahan tata letak posisi riwayat login/cookie
4. Mengganti foto di bagian profile karena dirasa kurang sesuai dari sebelumnya
AI sempat menebak penyebab yang salah juga Saat editor mendapat 404, awalnya diarahkan ke masalah izin, padahal penyebabnya URL yang saya ketik manual dengan UUID tidak valid. Saya baru menemukan penyebab sebenarnya setelah mencoba lewat tombol di halaman
Saya juga memutuskan sendiri untuk tetap memakai teknik yang diajarkan di tutorial ketika AI menawarkan pendekatan lain yang belum saya pahami
## Refleksi Proses
Selama proses ini saya jadi paham peran user dalam suatu web dengan pembagian peran authorization siapa yang bisa melakukan ini siapa yang tidak dan saya jadi lebih tau bahwa EndPoint JSON penulisan dan implementasinya harus hati-hati dari data sensitif.


## Tugas 5
1. Debouncing ini teknik menunda eksekusi fungsi sampai pengguna berhenti melakukan input selama waktu tertentu. Pada fitur pencarian AJAX, gunanya supaya setiap karakter yang diketik tidak langsung mengirim request ke server. Jadi request hanya dikirim setelah pengguna selesai ketik beberapa saat hingga kurangi jumalah req dan buat pencarian lebih efisien
2. await digunakan untuk menunggu Promise dari fetch() selesai sebelum kode dilanjutkan ke baris berikutnya. Dengan begitu, kita bisa menggunakan hasil dari request tersebut dengan benar. Kalau tidak pakai fecth() jalan di belakang layar dan kode berikutnya dijalankan tanpa tunggu hasil jadi hasil response belum tentu tersedia saat dibutuhkan
3. XSS adalah serangan ketika seseorang sisipkan kode JavaScript berbahaya dalam data yang kemudian dijalankan di browser pengguna lain.
Jadi Django template udah membantu melakukan escaping, sedangkan ketika data dirender lewat JavaScript kita lakukan pelrindungan XSS sendiri, contoh dengan escapeHtml() atau dengan textContent
## Strategi Prompting
Saya menanyakan hal yang menurut saya perlu diklarifikasi seperti pembuatan AJAX dan kolom search bar debouncing untuk bagian section education
## AI Disclosure
Saya menggunakan Claude (Anthropic) dan Deepseak sebagai bantuan dalam beberapa bagian tugas ini, dengan rincian sebagai berikut:
1. Menjelaskan strategi refactor untuk section education
2. Apa yang perlu dipertimbangkan untuk mengimplementasi yang dipelajari di tutorial dengan tugas ini
3. Membantu aku menyusun bagian yang perlu diubah dan tata letaknya
## Bagian yang saya kerjakan sendiri :
1. Menulis code pengisian dengan AJAX pada code education berpaku pada bagian project yang dikerjakan di tutorial
2. Menanmbahkan seacrh bar dan star untuk bagian education
3. Mengatur debouncing 300 milidetik sama seperti tutorial
4. Membuat form modal untuk education
5. Saya pakai CSS existing dari Tugas 3–4 tanpa bantuan AI
6. Saya test end-to-end di browser, cek DevTools, cek XSS payload
## Refleksi Proses
Saya menemukan route `create_education_ajax` belum terdaftar setelah AI memberi view-nya. Saya tambahkan sendiri path-nya dan memastikan import-nya lengkap. AI cenderung membuat pola baru daripada mengikuti konvensi yang sudah ada, sehingga berisiko menciptakan inkonsistensi, jadi saya berusaha untuk merefactor mandiri kali ini karena ingin belajar juga untuk persiapan kuis 2


## Tugas 6
1. REST adalah gaya arsitektur antarmuka perangkat lunak berbasis client-server yang seragam (uniform interface) dan stateless. Mengembalikan JSON saja belum tentu RESTful jika tidak memenuhi prinsip stateless, pemisahan resource via URI, penggunaan HTTP verb standar, dan status code semantik (Richardson Maturity Model Level 2). PUT digunakan untuk mengganti seluruh isi resource (wajib kirim semua field) sedangkan PATCH digunakan untuk modifikasi parsial (hanya field tertentu yang ingin diubah)
2. Serializer bertindak sebagai penerjemah dua arah: mengubah objek Django ORM menjadi JSON (serialization) serta memparsing dan memvalidasi JSON dari request menjadi instance model (deserialization). Dibandingkan JsonResponse manual, ModelSerializer otomatis memetakan field model, mengotomatisasi validasi skema (unique, max_length), menyediakan fungsi create() dan update() bawaan, serta mengembalikan error 400 otomatis jika data tidak valid
3. Autentikasi memastikan identitas pengguna (“Siapa Anda?”, menghasilkan request.user), sedangkan Otorisasi/Permission menentukan hak akses pengguna tersebut (“Apa yang boleh Anda lakukan?”). Autentikasi selalu dievaluasi lebih dulu, baru disusul otorisasi sebelum view dijalankan. Pemeriksaan wajib ada di server (backend) karena endpoint API bisa ditembak langsung (misal via cURL/Postman) tanpa melalui antarmuka HTML, menyembunyikan tombol di tampilan klien sama sekali tidak menjamin keamanan data
4. Pada SessionAuthentication, kredensial dikirim otomatis via cookie browser sehingga rentan terhadap serangan Cross-Site Request Forgery (CSRF). Oleh sebab itu, DRF mewajibkan token CSRF (via header X-CSRFToken) pada method mutasi data (POST, PUT, PATCH, DELETE). Pada pengujian, force_authenticate dipakai untuk menyimulasikan user yang sudah login secara instan tanpa alur login nyata dan membypass validasi CSRF agar tes fokus pada logika view. Namun, cara ini tidak menguji alur pengiriman token CSRF yang sebenarnya
## Strategi Prompting
Saya menggunakan pendekatan mendefinisikan kebutuhan endpoint API, field serializer, dan hak akses (permission) terlebih dahulu sebelum meminta AI cek hasil kerja saya
## AI Disclosure
Saya menggunakan Claude sebagai bantuan dalam beberapa bagian tugas ini, dengan rincian sebagai berikut:
1. Scaffolding awal struktur ModelSerializer dan @api_view untuk modul Education, Experience, dan Project
2. Membantu mengimplementasikan animasi JavaScript untuk academic journey timeline dan morphing hamburger menu.
3. Membantu refaktor dan konsolidasi style.css agar seluruh variabel warna, font, dan shadow terpusat di :root tanpa aturan redundan
4. Meminta langkah-langkah cara bagaimana bisa melakukan test case API sebagai superuser dan user biasa
## Bagian yang saya kerjakan sendiri :
1. Menganalisis dan memperbaiki kegagalan 3 unit test lama (test_experience_page, test_empty_experience_page, test_completed_experience)
2. Menemukan dan memperbaiki bug logo universitas yang terpotong akibat perubahan JS oleh AI
3. Memutuskan desain visual keseluruhan: tema akademik journey roadmap dengan teal connector beam dan live pulse dot untuk milestone universitas yang sedang berlangsung
4. Melakukan pengujian menyeluruh di browser (lokal) dan DevTools untuk memastikan 43 test lolos dan semua endpoint API berjalan sesuai ekspektasi
## Refleksi Proses
Tugas 6 membuat saya benar-benar memahami bahwa DRF bukan sekadar cara baru menulis view, melainkan pergeseran paradigma dari halaman yang dirender server menjadi API yang dikonsumsi klien, dan memahami perbedaan ini langsung terasa saat harus memperbaiki unit test lama yang asumsinya tidak lagi berlaku setelah transisi ke arsitektur asinkronus