from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="PEA Stakeholder Map",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ลดพื้นที่ว่างรอบหน้าเว็บ
st.markdown(
    """
    <style>
    .block-container,
    .stMainBlockContainer {
        max-width: 100% !important;
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
        padding-top: 3.5rem !important;
        padding-bottom: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = (
    Path(__file__).parent
    / "pea_stakeholder_power_interest_map_9.html"
)

html = html_path.read_text(encoding="utf-8")
components.html(html, height=1100, scrolling=True)
