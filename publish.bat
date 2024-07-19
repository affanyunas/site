@echo off
cd ./content/post

REM Menyimpan URL remote saat ini dalam variabel
for /f "tokens=2 delims= " %%i in ('git remote get-url origin') do set CURRENT_URL=%%i

REM URL remote yang diinginkan
set DESIRED_URL=https://github.com/affanyunas/site.git

REM Memeriksa apakah URL remote saat ini sesuai dengan URL yang diinginkan
if "%CURRENT_URL%" neq "%DESIRED_URL%" (
    echo URL remote tidak sesuai. Mengubah URL remote ke %DESIRED_URL%
    git remote set-url origin %DESIRED_URL%
) else (
    echo URL remote sudah benar: %CURRENT_URL%
)

REM Menambahkan semua file yang diubah ke git
git add .

REM Membuat commit dengan pesan "Post"
git commit -m "Post"

REM Mengirimkan perubahan ke branch main di remote repository
git push origin main

REM Kembali ke direktori root proyek
cd ..

REM Menunggu selama 1 detik sebelum keluar
timeout /t 1

REM Keluar dari script
exit
