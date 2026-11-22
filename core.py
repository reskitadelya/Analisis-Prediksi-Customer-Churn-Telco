"""core.py - fungsi bersama untuk seluruh halaman Streamlit."""
import joblib
import pandas as pd
import streamlit as st

from train_model import DATA_PATH, MODEL_PATH, TARGET, load_data

ANGGOTA = [("Reskita Delya Rumaday", "241011402496"),
           ("Feni Iza Tulnisa", "241011400626"),
           ("Ifat Mardyah", "241011400632")]
DOSEN = "Farizi Ilham, M.Kom."
COLORS = {"Yes": "#E4572E", "No": "#2F6FED"}

CSS = """
<style>
.block-container{max-width:920px;padding-top:2.5rem}
[data-testid="stMetric"]{background:#fff;border:1px solid #D6E2F7;border-radius:12px;padding:12px 16px}
[data-testid="stMetricLabel"] p{font-size:.75rem}
.card{background:#fff;border:1px solid #D6E2F7;border-radius:12px;padding:14px 16px;height:100%}
.card h5{margin:0 0 .6rem;font-size:.85rem;color:#1B2A41}
.card p{margin:0;font-size:.8rem;color:#33415c;line-height:1.55}
.card .sub{color:#8a97ad;font-size:.72rem;margin-top:.5rem}
</style>
"""


def inject_css():
    st.markdown(CSS, unsafe_allow_html=True)


def card(title: str, body: str, sub: str = "") -> str:
    s = f'<div class="sub">{sub}</div>' if sub else ""
    return f'<div class="card"><h5>{title}</h5><p>{body}</p>{s}</div>'


@st.cache_data
def get_df() -> pd.DataFrame:
    df = load_data(DATA_PATH)
    df["Churn"] = df[TARGET]
    return df


@st.cache_resource
def get_art():
    if not MODEL_PATH.exists():
        return None
    try:
        return joblib.load(MODEL_PATH)
    except Exception as e:  # biasanya beda versi scikit-learn / imbalanced-learn
        st.error("File model gagal dibuka (kemungkinan beda versi library). "
                 "Jalankan ulang `python train_model.py` lalu muat ulang halaman.")
        st.caption(f"Detail: {e}")
        return None


def require_art():
    art = get_art()
    if art is None:
        st.error("Model belum tersedia. Jalankan `python train_model.py` terlebih dahulu.")
        st.stop()
    return art


def risk_label(p: float) -> tuple[str, str]:
    if p >= 0.7:
        return "TINGGI", "🔴"
    if p >= 0.4:
        return "SEDANG", "🟠"
    return "RENDAH", "🟢"


def metrics_table(art, key="tuned") -> pd.DataFrame:
    rows = []
    for name, r in art["results"].items():
        m = r[key]
        rows.append({"Model": name, "Accuracy": m["accuracy"], "Precision": m["precision"],
                     "Recall": m["recall"], "F1": m["f1"], "ROC-AUC": m["roc_auc"]})
    return pd.DataFrame(rows).set_index("Model")
