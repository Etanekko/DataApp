import streamlit as st
st.title("Ma première application Streamlit")
st.write("Bienvenue dans ce cours !")
nom = st.text_input("Quel est votre nom ?")

if nom:
    st.success(f"Enchanté,{nom} !")
age = st.slider("Quel est votre age ?", 0 , 120 , 25)
st.write(f"Vous avez {age} ans")
genre = st.radio("Quel est votre genre ?", ["Homme", "Femme"])
st.write(f"Genre choisi : {genre}")
if st.button("Cliquez ici"):
    st.balloons()
st.file_uploader("umpoald file")
nombre =st.number_input("Entrer votre")
job =st.checkbox("quel est votre job ") 
st.write(f"{job}")
option = st.selectbox(
    'Choose your favorite color',
    ['Red', 'Blue', 'Green', 'Yellow']
)
st.write('Your selected color:', option)

import pandas as pd
import numpy as np
df = pd.DataFrame(
np.random.randn(10, 3),
columns=['Colonne A', 'Colonne B', 'Colonne C']
)
st.subheader("Tableau de données")
st.dataframe(df)
st.subheader("Graphique en courbes")
st.line_chart(df)



