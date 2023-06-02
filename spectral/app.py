import os
from pathlib import Path
import streamlit as st


st.set_page_config(layout='wide')

# The following must retrieve path: `/home/sites/spectral/spectral`
APP_DIRPATH = Path(__file__).resolve().parents[0]

os.path.join(ASSETS_DIRPATH, 'SITESspectral_LOGO_254x251.png')

st.write(APP_DIRPATH)
