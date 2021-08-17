import numpy as np
import pandas as pd
import streamlit as st


uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg'])
if uploaded_file is not None:
    file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
    st.write(file_details)