@echo off
setlocal

:: URL remote yang diinginkan
set DESIRED_URL=https://github.com/tuanona/site.git

:: Pindah ke direktori yang berisi file yang akan di-commit
cd /d .\content\post

:: Menyimpan URL remote saat ini dalam variabel
for /f "tokens=*" %%i in ('git remote get-url origin') do set current_url=%%i

:: Memeriksa apakah URL remote saat ini sesuai dengan URL yang diinginkan
if /i "%current_url%" neq "%DESIRED_URL%" (
    echo URL remote tidak sesuai. Mengubah URL remote ke %DESIRED_URL%
    git remote set-url origin %DESIRED_URL%
) else (
    echo URL remote sudah benar: %current_url%
)

:: Menambahkan semua file yang diubah ke git
git add .

:: Membuat commit dengan pesan "Post"
git commit -m "Post"

:: Mengirimkan perubahan ke branch main di remote repository
git push origin main

:: Kembali ke direktori root proyek
cd /d ..\..

:: Menunggu selama 2 detik sebelum keluar
timeout /t 2

:: Menampilkan pesan Complete
echo Complete

exit
