import streamlit as st
import requests
from streamlit_lottie import st_lottie
import pandas as pd
import plotly.express as px

#----------Titulo
st.set_page_config(page_title="Programas Internacionales TEC", page_icon=":globe_with_meridians:", layout="wide")
st.title("Graficas de Sankey :u7a7a:")


#CSV

df = pd.read_csv('limpiezafinal.csv')

#FILTROS

nivel = st.selectbox(
    "Selecciona el nivel:",
    options = df["Nivel"].unique()
)

df1_selection = df[
    (df['Nivel'] == nivel) 
]

#Funcion Sankey
SAKY3 = px.parallel_categories(df1_selection,
                                dimensions= ['Area Academica','ContinenteOportunidadAsignada','TipoPrograma'],
                                color = df1_selection['NumCont'],
                                color_continuous_scale = px.colors.sequential.Aggrnyl)
st.write(SAKY3)
