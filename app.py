import numpy as np
import pandas as pd
import cv2
import streamlit as st


uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg'])
if uploaded_file is not None:
    file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
    st.write(file_details)

if uploaded_file is not None:
    with open(uploaded_file.name,'wb') as f:
        f.write(uploaded_file.read())

st.write(f)