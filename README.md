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