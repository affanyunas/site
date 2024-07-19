import subprocess
import time
import sys

# Fungsi untuk menjalankan perintah shell dan mendapatkan output
def run_command(command):
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error running command: {result.stderr}")
        sys.exit(result.returncode)
    return result.stdout.strip()

# URL remote yang diinginkan
DESIRED_URL = "https://github.com/affanyunas/site.git"

# Pindah ke direktori yang berisi file yang akan di-commit
subprocess.run("cd ./content/post", shell=True)

# Menyimpan URL remote saat ini dalam variabel
current_url = run_command("git remote get-url origin")

# Memeriksa apakah URL remote saat ini sesuai dengan URL yang diinginkan
if current_url != DESIRED_URL:
    print(f"URL remote tidak sesuai. Mengubah URL remote ke {DESIRED_URL}")
    run_command(f"git remote set-url origin {DESIRED_URL}")
else:
    print(f"URL remote sudah benar: {current_url}")

# Menambahkan semua file yang diubah ke git
run_command("git add .")

# Membuat commit dengan pesan "Post"
run_command('git commit -m "Post"')

# Mengirimkan perubahan ke branch main di remote repository
run_command("git push origin main")

# Kembali ke direktori root proyek
subprocess.run("cd ..", shell=True)

# Menunggu selama 1 detik sebelum keluar
time.sleep(1)
