import streamlit as st

st.set_page_config(page_title="Chem-Calc", page_icon="🧪", layout="wide")

# Gaya ala Valorant
st.markdown("""
    <style>
    body {
        background-color: #0e0e10;
        color: #ffffff;
    }
    .title {
        text-align: center;
        font-size: 60px;
        font-weight: bold;
        color: #f94144;
        margin-top: 2em;
    }
    .subtitle {
        text-align: center;
        font-size: 20px;
        margin-bottom: 3em;
        color: #ddd;
    }
    .start-button {
        display: flex;
        justify-content: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>CHEM-CALC</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Kalkulator Berat Molekul | IUPAC 2007</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Tombol ke halaman kalkulator
st.markdown("<div class='start-button'>", unsafe_allow_html=True)
if st.button("🔬 KALKULATOR ADA DISINI", use_container_width=True):
    st.switch_page("pages/Kalkulator_BM.py")
st.markdown("</div>", unsafe_allow_html=True)
