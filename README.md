# Prediksi Churn Pelanggan Telco (Streamlit, 10 halaman)

Struktur: app.py (navigasi), core.py, train_model.py, views/ (10 halaman), data/, model/, .streamlit/, DEPLOY.md

## Menjalankan
1. `py -3.12 -m venv venv`
2. `.\venv\Scripts\python.exe -m pip install --default-timeout=100 --retries 10 -r requirements.txt`
3. `.\venv\Scripts\python.exe train_model.py`   (opsional; model sudah disertakan, wajib bila muncul error versi)
4. `.\venv\Scripts\python.exe -m streamlit run app.py`

## Fitur pengembangan
- A. Simulator "bagaimana jika" (halaman Prediksi Satu Pelanggan)
- B. Kestabilan model (CV rata-rata ± std) dan studi ablasi SMOTE/PCA (halaman Modelling & Evaluasi)
- C. Kalkulator Untung-Rugi Retensi (halaman baru)
- D. Deploy: lihat DEPLOY.md
