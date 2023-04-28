from pathlib import Path
import streamlit as st

st.set_page_config(layout='wide')

APP_DIRPATH = Path(__file__).resolve().parents[0]
st.write(APP_DIRPATH)
