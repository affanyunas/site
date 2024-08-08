Title: Mengatasi Tantangan dengan Pergeseran Paradigma: Pengalaman Pengembangan CLI
Date:2024-08-08  
Category: Teknologi  
Tags: Web Development, CLI Development, Go, Rust  
Authors: Affan Yunas  
Summary: Proyek `nftfetch` memberikan banyak pelajaran tentang efisiensi dan pemecahan masalah dengan pendekatan yang berbeda dalam pengembangan perangkat lunak.  
Description: Dalam perjalanan mengembangkan `nftfetch`, berbagai tantangan teknis dan pemikiran baru muncul, khususnya dalam peralihan dari Rust ke Go dan pemahaman tentang problem X dan Y. Artikel ini membahas pengalaman tersebut dan pandangan baru yang diperoleh.

### Pendahuluan

Proyek `nftfetch` yang sedang saya kerjakan membawa banyak pelajaran dan wawasan menarik. Awalnya, saya memutuskan untuk menggunakan Rust untuk menulis kode. Namun, ketika harus membaca dan menulis file, Rust membuat saya frustrasi dengan penanganan error yang cerewet. Dengan waktu yang terbatas, saya memutuskan untuk mencoba Go, sebuah bahasa yang belum pernah saya gunakan sebelumnya.

### Transisi dari Rust ke Go

Pengalaman pertama saya dengan Go sangat mengesankan. Kode yang saya tulis terasa seperti kumpulan paket yang terorganisir dengan baik. Go memungkinkan import dependensi dari berbagai sumber dengan mudah, membuatnya sangat fleksibel. Selain itu, keberadaan `go.mod` dan `go.sum` sangat membantu dalam mengelola dependensi proyek. Dalam dua hari, saya berhasil membuat CLI saya dengan dua argumen yang berjalan dengan lancar. Ini adalah pengalaman yang sangat memuaskan.

### Pendekatan Baru dalam Menghadapi Masalah

Salah satu hal paling berharga yang saya pelajari adalah cara Go menangani masalah. Alih-alih memisahkan setiap masalah menjadi bagian-bagian kecil yang rumit, Go mengajarkan saya untuk menangani masalah sebagai satu kesatuan dan memberikan error jika diperlukan. Pendekatan ini membuat saya melihat setiap tantangan sebagai sebuah bundle yang dapat diatasi secara komprehensif, tanpa perlu membaginya menjadi potongan-potongan yang lebih kecil.

### X dan Y Problem dalam Pemecahan Masalah

Pemikiran ini juga membawa saya pada pemahaman tentang masalah X dan Y yang terkenal. Seringkali, kita terjebak dalam upaya menyelesaikan masalah Y tanpa menyadari bahwa akar masalah sebenarnya adalah X. Pandangan ini sangat membuka mata saya. Dengan pemahaman ini, saya mulai mengidentifikasi masalah utama sebelum mencoba menyelesaikan gejala-gejalanya. Ini membantu saya menjadi lebih efektif dalam pemecahan masalah.

### Masa Depan Pengembangan CLI

Dengan semua pelajaran ini, saya terus maju dalam mengembangkan `nftfetch`. Setiap tantangan yang muncul saya hadapi dengan pendekatan baru yang lebih efisien dan terstruktur. Pengalaman ini tidak hanya meningkatkan kemampuan teknis saya tetapi juga membawa perubahan positif dalam cara saya memandang dan menyelesaikan masalah.

### Hal Baru

Perjalanan mengembangkan `nftfetch` memberikan banyak pelajaran berharga. Dari peralihan dari Rust ke Go, hingga pemahaman mendalam tentang X dan Y problem, semua ini memberikan wawasan baru yang meningkatkan efisiensi dan efektivitas dalam pengembangan perangkat lunak. Dengan fokus pada optimasi dan pendekatan yang lebih holistik dalam menghadapi masalah, saya yakin proyek ini akan terus berkembang dengan baik.

