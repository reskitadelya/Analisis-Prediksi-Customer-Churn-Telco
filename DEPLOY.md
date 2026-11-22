# Deploy ke Streamlit Community Cloud

1. Buat akun di https://github.com dan repositori baru (Public) bernama `telco-churn-app`.
2. Dari folder proyek, jalankan di terminal:
   ```
   git init
   git add .
   git commit -m "Telco churn app"
   git branch -M main
   git remote add origin https://github.com/<username>/telco-churn-app.git
   git push -u origin main
   ```
   Pastikan folder `data/` dan `model/` ikut ter-push (`venv/` tidak, sudah diatur di `.gitignore`).
3. Buka https://share.streamlit.io, login dengan GitHub, klik **Create app**.
4. Pilih repositori `telco-churn-app`, branch `main`, file utama `app.py`.
5. Klik **Advanced settings**, pilih **Python 3.12**, lalu **Deploy**.
6. Tunggu beberapa menit. Salin tautan `https://....streamlit.app` untuk dosen.

Jika muncul "File model gagal dibuka": latih ulang di komputer Anda (`python train_model.py`)
dengan versi library yang sama seperti `requirements.txt`, lalu push ulang folder `model/`.
