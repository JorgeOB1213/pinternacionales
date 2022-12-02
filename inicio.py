import streamlit as st
import requests
from streamlit_lottie import st_lottie
import pandas as pd
import plotly.express as px

#Configuración de pag

st.set_page_config(page_title="Programas Internacionales TEC", page_icon=":globe_with_meridians:", layout="wide")

#función imagenes gif

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#descarga de csv

df = pd.read_csv('programasinternacionalesotros2.csv')


#PAGES 

st.sidebar.success("Selecciona la pagina")
# Descargas 
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/datafiles/AtGF4p7zA8LpP2R/data.json")
lottie_coding2 = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_90lERnu6WV.json")

# ---Encabezado -----

with st.container():
    st.subheader("Jorge Oviedo Barrera A01702048")
    st.title("Programas Internacionales TEC :chart_with_upwards_trend::globe_with_meridians::airplane::chart_with_downwards_trend:")
    st.write("En esta webapp se puede visualizar y entender la situación en la que se encuentran los programas internacionales lo cual nos ayudará a comprender mejor la manera el status de los estudiantes para poder hacer un mejor análisis.")
left_column, right_column = st.columns(2)
with left_column:
    st_lottie(lottie_coding, height=300, key="coding")
with right_column:
    st_lottie(lottie_coding2, height=300, key="coding2")

#graficas 

with st.container():
    st.write("---")

st.header("DB con el que se trabajara")

#FILTROS

paisasignado = st.multiselect(
    "Selecciona los paises asignados :",
    options = df["PaisAsignado"].unique(),
    default = list(df["PaisAsignado"].unique())[0]
)

campus = st.multiselect(
    "Selecciona los campus que deseas visualizar :",
    options = df["CampusAdministrador"].unique(),
    default = list(df["CampusAdministrador"].unique())[0]
)

nivel = st.multiselect(
    "Selecciona el nivel de educación :",
    options = df["Nivel"].unique(),
    default = list(df["Nivel"].unique())[0]
)
df_selection = df.query(
    "PaisAsignado == @paisasignado & CampusAdministrador == @campus & Nivel == @nivel "
)
#st.dataframe(df_selection)

st.write("---")

#----------KPI---------------
st.subheader(":bar_chart: Indicadores")
st.markdown("##")

#indicadores funciones 
Can = int(df_selection["PrimeraOpcion"].count())
primera_total = round(df_selection["PuntajeAsignaciÃ³n"].mean(),2)


df_p = df_selection.groupby(['Intercambio Internacional','PrimeraOpcion']).size().reset_index()
df_p.columns = ['Intercambio Internacional','PrimeraOpcion' ,'Counts']
df_p['percentage'] = df_p.groupby(['Counts']).size().groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
df_p.columns = ['Oportunidad','PrimeraOpcion' ,'Counts', 'Percentage']
df_p['Percentage'] = (df_p['Counts'] / df_p['Counts'].sum()) * 100
#df_p
total_int =  df_p.iloc[2,2]
total_study = df_p.iloc[1,2]
total_1 = round(((total_int + total_study)*100)/Can,2)

TT_int = df_p.iloc[0,2] + df_p.iloc[1,2]
TT_study = df_p.iloc[2,2] + df_p.iloc[3,2]
P_TTint = round((TT_int*100)/Can,2)
P_TTstudy = round((TT_study*100)/Can,2)
#Columnas de kip

left_column1,middle_column1 ,right_column1 = st.columns(3)
with left_column1:
    st.subheader("Cantidad de registros ")
    st.subheader(f"{Can:,} registros")

with middle_column1:
    st.subheader("Porcentaje de asignados a 1° opción (intercambio y Study Abroad): ")
    st.subheader(f"{total_1:,}%")

with right_column1:
    st.subheader("Promedio puntaje de asignación: ")
    st.subheader(f"{primera_total:,}")

left_column2,middle_column2 ,right_column2 = st.columns(3)
with left_column2:
    st.subheader("Diferencia estudiantes Study Abroad y Intercambios ")
    st.subheader(f"{TT_study:,} / {TT_int:,}")
with middle_column2:
    st.subheader("Porcentaje de estudiantes que se fueron de intercambio: ")
    st.subheader(f"{P_TTint:,}%")
with right_column2:
    st.subheader("Porcentaje de estudiantes que se fueron de Study Abroad: ")
    st.subheader(f"{P_TTstudy:,}%")


