import numpy as np
import pandas as pd
import streamlit as st


st.title('ВОУ!')
st.text('Привет, Ваня, вот создал какую-то хуету, может быть мы сможем использовать это для тестирования приложений или развертки приложений.')

data = np.array([1,2,3])

st.bar_chart(data)