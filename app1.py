import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests


st.markdown("<h1 style='text-align: left; color: blue;'>SCRAPPER DATA</h1>", unsafe_allow_html=True)

st.markdown("""
This app allows you to download scraped data on motocycles from expat-dakar 
* **Python libraries:** base64, pandas, streamlit
* **Data source:** [Expat-Dakar](https://www.expat-dakar.com/).
""")


# Fonction de loading des données
def load_(dataframe, title, key) :
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    if st.button(title,key):
      
        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe)

# définir quelques styles liés aux box
st.markdown('''<style> .stButton>button {
    font-size: 12px;
    height: 3em;
    width: 25em;
}</style>''', unsafe_allow_html=True)

# Charger les données 
load_(pd.read_csv('data/Chien_scrapper.csv'), 'Chien', '1')
load_(pd.read_csv('data/Mouton_scrapper.csv'), 'Mouton', '2')
load_(pd.read_csv('data/Lapin_et_Pigeon_scrapper.csv'), 'Lapin et Pigeon', '3')
load_(pd.read_csv('data/Autre_animaux_scrapper.csv'), 'Autre animaux', '4')
