Title: Evolusi Bahasa Pemrograman: Dampak Lisp dan Fortran
Date:2024-07-19 12:00
Category: Teknologi
Tags: Lisp, Fortran, Bahasa Pemrograman
Authors: Affan Yunas
Summary: Artikel ini membahas evolusi bahasa pemrograman dari Lisp ke C, mengeksplorasi bagaimana perdebatan awal mempengaruhi teknologi pemrograman modern.
Description: Artikel ini menjelajahi perjalanan evolusi bahasa pemrograman dari awal mula Lisp, yang diperkenalkan pada tahun 1958, hingga bahasa seperti C yang muncul pada 1970-an. Dengan fokus pada perdebatan antara Lisp dan Fortran, artikel ini menjelaskan bagaimana pilihan teknologi awal membentuk paradigma pemrograman saat ini. Dari struktur simbolik Lisp hingga model prosedural Fortran dan C, artikel ini memberikan wawasan mendalam tentang bagaimana perkembangan ini mempengaruhi bahasa pemrograman modern seperti Python dan Java.

### Pengaruh Kemenangan Fortran

Salah satu poin penting dalam sejarah pemrograman adalah kemenangan Fortran atas Lisp. Hal ini memiliki dampak besar pada pengembangan hardware komputer. Seandainya Lisp yang menang, hardware bisa saja dikembangkan untuk mendukung fitur-fitur seperti yang ada di Lisp. Namun, karena Fortran yang menang, model pemrograman yang mirip dengan Assembly seperti yang dimiliki C menjadi model default.

### Dekat dengan Hardware: Lisp vs C

Seringkali kita mendengar bahwa "C adalah pembungkus tipis pada kode mesin." Namun, perlu diingat bahwa kons, car, cdr, eq, cond adalah instruksi level mesin di Lisp. Misalnya, car = "contents address register" dan cdr = "contents decrement register". S-expression di Lisp sebenarnya adalah pohon sintaks yang sederhana. Jadi, jika ingin berbicara tentang mendekatkan diri pada hardware, kita harus mengakui peran Lisp. Ini hanyalah kecelakaan sejarah bahwa hardware bergerak menjauh dari Lisp menuju dunia Fortran yang lebih berfokus pada manipulasi bit.

### Akibat dari Sejarah: Dunia Fortran yang Rumit dan Rawan Kesalahan

Model pemrograman yang kita miliki saat ini, yang cenderung rumit, rawan kesalahan, dan lemah dalam pengecekan, adalah hasil dari kecelakaan sejarah dalam investasi pada level hardware dan apa yang dianggap praktis oleh industri. Artikel "worse is better" menggambarkan bagaimana pendekatan yang lebih praktis seringkali mengalahkan desain yang lebih baik.

### Refleksi

Evolusi bahasa pemrograman adalah proses yang tak henti-hentinya. Bahasa-bahasa baru terus bermunculan, masing-masing dengan kelebihan dan kekurangannya sendiri. Para programmer harus terus belajar dan beradaptasi dengan bahasa-bahasa baru ini untuk tetap relevan di dunia yang terus berubah. Meskipun Lisp tidak menjadi bahasa dominan, pengaruhnya masih terasa dalam bahasa-bahasa fungsional modern, seperti Haskell dan Erlang.

