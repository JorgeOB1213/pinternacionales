import streamlit as st
import requests
from streamlit_lottie import st_lottie
import pandas as pd
import plotly.express as px

#-----FORMATOPAGINA--------

st.set_page_config(page_title="Programas Internacionales TEC", page_icon=":globe_with_meridians:", layout="wide")
st.header("Mapas :earth_africa:")

#descarga de csv

df1 = pd.read_csv('limpiezafinal.csv')

#Filtros

nivel = st.selectbox(
    "Selecciona el nivel:",
    options = df1["Nivel"].unique()
)

areaac = st.selectbox(
    "Selecciona el area academica :",
    options = df1["Area Academica"].unique()
)

campus1 = st.selectbox(
    "Selecciona la región de campus que desea ver :",
    options = df1["RegionCampus"].unique()
)

df1_selection = df1[
    (df1['Area Academica'] == areaac) &
    (df1['RegionCampus'] == campus1) &
    (df1['Nivel'] == nivel) 
]

#Mapa mamalon

counts = df1_selection.PaisOportunidadAsignada.value_counts().rename_axis('PaisOportunidadAsignada').reset_index(name='CantidadEstudiantes')
map4 = px.choropleth(counts, locations="PaisOportunidadAsignada",
                    color="CantidadEstudiantes",
                    hover_name="PaisOportunidadAsignada",
                    color_continuous_scale=px.colors.colorbrewer.RdYlGn,
                    projection='orthographic')

st.write(map4)