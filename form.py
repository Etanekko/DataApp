import streamlit as st
import pandas as pd

def show_sheets_page():
    st.title("Lecture de Google Sheets dans Streamlit")

    # Remplace cet ID par celui de ta feuille Google Sheets
    sheet_id = "1TGgTeXY0sbMvi1wtK4jm4ekNH0GcL9LbEnZfBsO6oKM"
    sheet_name = "AppSheet"
    url = f"https://docs.google.com/spreadsheets/d/1TGgTeXY0sbMvi1wtK4jm4ekNH0GcL9LbEnZfBsO6oKM/gviz/tq?tqx=out:csv&sheet=AppSheet"

    try:
        df = pd.read_csv(url)
        st.success("Données chargées avec succès depuis Google Sheets !")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Erreur lors du chargement des données : {e}")
show_sheets_page()