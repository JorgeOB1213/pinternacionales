import pandas as pd

df = pd.read_csv('programas_internacionales_final1.csv')
df['NumCont'] = ''

for i in range(len(df)):
    if df['ContinenteOportunidadAsignada'][i] == 'Africa':
        df['NumCont'][i] = 1
    elif df['ContinenteOportunidadAsignada'][i] == 'America Norte':
        df['NumCont'][i] = 2
    elif df['ContinenteOportunidadAsignada'][i] == 'America Sur':
        df['NumCont'][i] = 3
    elif df['ContinenteOportunidadAsignada'][i] == 'Asia':
        df['NumCont'][i] = 4
    elif df['ContinenteOportunidadAsignada'][i] == 'Eurasia':
        df['NumCont'][i] = 5
    elif df['ContinenteOportunidadAsignada'][i] == 'Europa':
        df['NumCont'][i] = 6
    elif df['ContinenteOportunidadAsignada'][i] == 'Indef':
        df['NumCont'][i] = 7
    elif df['ContinenteOportunidadAsignada'][i] == 'Oseania':
        df['ContinenteOportunidadAsignada'][i] = 'Oceania'
        df['NumCont'][i] = 8
df.to_csv("Limpiezafinal.csv")