Buka aplikasi Qna Musik dan jalan kan local server di http://127.0.0.1:8000/ (saya menggunakan waitress untuk Web Server Gateway Interface nya di aplikasi Python)
Aplikasi ini adalah aplikasi kuis mengenai musik. 
User atau player mengisi pertanyaan d bagian chapter 1 terlebih dahulu mulai dari pertanyaan 1 sampai 5. (user bisa mengakses ke pertanyaan ke 2 apabila user telah menjawab pertanyaan nomer 1), (Jika user tidak menjawab sama sekali maka tombol next terkunci)
pada soal nomer 2 ada button kembali dan next (buton kembali bisa diakses namun user tidak bisa memilih kembali jawaban nya) hanya bisa sekali pilihan saja.
selesai user menjawab pertanyaan di soal nomer 5 akan ada button untuk menampilkan hasil atau jawaban yang benar dari semua pertanyaan, jika user telah memilih namun pertanyaan nya salah akan dimunculkan notifikasi " Soal nomer 5 salah jawban yang benar adalah Gitar" 
Setelah user menekan button "Lihat Jawbaan" maka button akan berubah menjadi next chapter
Chapter 2 muncul dan menampilkan soal kembali ke tahap berikutnya yang lebih susah.
Menampilkan soal dengan gambar.
