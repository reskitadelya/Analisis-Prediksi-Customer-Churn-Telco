import streamlit as st

from core import ANGGOTA, DOSEN, card, get_art, get_df

df, art = get_df(), get_art()
churn_rate = (df["Churn"] == "Yes").mean()

st.title("Analisis & Prediksi Customer Churn Telco")
st.caption("Implementasi Machine Learning berbasis web dengan Streamlit untuk menganalisis dan memprediksi potensi Customer Churn.")
st.markdown(
    "Aplikasi ini memaparkan seluruh tahapan proyek **prediksi pelanggan yang akan berhenti "
    "berlangganan (churn)** pada dataset *IBM Telco Customer Churn*. Alurnya dimulai dari "
    ":blue[pengenalan data] dan :blue[eksplorasi], dilanjutkan :orange[preprocessing] "
    "(data hilang, *data leakage*, ketidakseimbangan kelas) dan :orange[reduksi dimensi (PCA)], "
    "lalu perbandingan :green[lima algoritma klasifikasi], hingga **prediksi langsung** "
    "yang dapat dicoba pengguna.")

st.markdown("**Tujuan proyek**")
st.markdown(
    f"- Mengidentifikasi faktor yang paling memengaruhi keputusan pelanggan untuk berhenti.\n"
    f"- Membangun model yang andal meski hanya **{churn_rate:.1%}** pelanggan yang churn.\n"
    f"- Menyediakan alat prediksi untuk satu pelanggan maupun banyak pelanggan sekaligus (CSV).")

best = art["best_model"] if art else "-"
auc = f"{art['results'][best]['tuned']['roc_auc']:.3f}" if art else "-"
c1, c2, c3, c4 = st.columns(4)
c1.metric("Jumlah pelanggan", f"{len(df):,}")
c2.metric("Churn rate", f"{churn_rate:.1%}")
c3.metric("Model terbaik (F1)", best)
c4.metric("ROC-AUC model terbaik", auc)

st.divider()
st.subheader("Alur pengerjaan")
n_cols = art["prep_info"]["n_cols_total"] if art else df.shape[1] - 1
pca_text = "Reduksi dimensi dengan PCA."
if art:
    p = art["pca_info"]
    pca_text = (f"{p['n_features']} fitur dipadatkan menjadi {p['k']} komponen "
                f"(selisih F1 vs tanpa PCA: {p['delta_f1_best']:+.3f}).")
cols = st.columns(4)
steps = [
    ("1. Dataset", f"Karakteristik data: {len(df):,} baris, {n_cols} kolom, klasifikasi biner."),
    ("2. EDA & Preprocessing", "Menangani data hilang, data leakage, ketidakseimbangan kelas, dan encoding."),
    ("3. Reduksi PCA", pca_text),
    ("4. Modelling", "Lima algoritma dibandingkan, di-tuning, lalu dipakai untuk prediksi."),
]
for col, (t, b) in zip(cols, steps):
    col.markdown(card(t, b), unsafe_allow_html=True)

st.markdown("**Mulai dari sini**")
l1, l2, l3 = st.columns(3)
l1.page_link("views/eda.py", label="Jelajahi data", icon=":material/bar_chart:")
l2.page_link("views/modelling.py", label="Lihat hasil model", icon=":material/model_training:")
l3.page_link("views/prediksi_satu.py", label="Coba prediksi", icon=":material/person_search:")

st.divider()
st.subheader("Anggota Kelompok 8")
cols = st.columns(3)
for col, (nama, nim) in zip(cols, ANGGOTA):
    col.markdown(card(nama, "", f"NIM {nim}"), unsafe_allow_html=True)
st.markdown(f"Dosen pengampu: **{DOSEN}**")
st.caption("Program Studi Informatika, Fakultas Ilmu Komputer, Universitas Pamulang")

with st.expander("Mengapa Memprediksi Churn Penting?"):
    st.markdown(
        f"""
        - **Mengurangi kehilangan pelanggan** dengan mengidentifikasi pelanggan yang berisiko berhenti lebih awal.
        - **Mendukung strategi retensi** agar perusahaan dapat memberikan penawaran atau layanan yang lebih tepat sasaran.
        - **Meningkatkan efisiensi bisnis** dengan memprioritaskan pelanggan yang memiliki risiko churn lebih tinggi.
        - Data churn hanya sekitar **{churn_rate:.1%}**, sehingga performa model tidak cukup dinilai dari akurasi saja.
        - Oleh karena itu, digunakan **Recall, F1-Score, dan ROC-AUC** untuk menilai kemampuan model dalam mendeteksi pelanggan yang berpotensi churn.
        """
    )