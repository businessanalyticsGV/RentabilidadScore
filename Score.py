#### 0.- PRELIMINARIES

import os
import pandas as pd
pd.set_option('display.max_columns',500)

path = os.getcwd().replace('\\','/')
#### 1.- EXTRACCIÓN Y LIMPIEZA RAPIDA
df = pd.read_csv('BaseDatos/Base_Trabajo_INT.csv')
ls_index = ['ReservationNumber','Mix_canal']
df_index = df[[c for c in df if c in ls_index]]
df = df[[c for c in df if c not in ls_index]]
df = df.drop(columns = ['Mix_NA_IN'], axis = 1)

ls_egresos = ['CostoHospedaje','Comisión',
               'Closing Cost','Promociones y Campañas','Ajuste_SC']

for eg in ls_egresos:
    df[eg] = df[eg]*-1

print(df.shape)
print(df.head())

print([(field,sum(pd.isnull(df[field]))) for field in df])

#### II.- SCORING

from TeamAM_Score import MemberScoring

score = MemberScoring()

df['scores'] = score.fit_score(df,cumulative_variance=.8)
df['ReservationNumber'] = df_index['ReservationNumber']
df['Mix_canal'] = df_index['Mix_canal']
df.to_csv(path+'/Score/RentabilidadScore.csv', index = False)