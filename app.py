from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="PEA Stakeholder Map",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .block-container,
    .stMainBlockContainer {
        max-width: 100% !important;
        padding: 3.5rem 0.5rem 0 !important;
    }

    /* ปรับความสูงกรอบเว็บตามหน้าต่าง */
    .stElementContainer:has(iframe) {
        height: calc(100dvh - 4.5rem) !important;
    }

    iframe {
        width: 100% !important;
        height: calc(100dvh - 4.5rem) !important;
        border: none;
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
components.html(html, height=650, scrolling=True)
