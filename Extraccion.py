import pandas as pd
import numpy as np
import os

path = os.getcwd().replace('\\','/')

Base_Rent = pd.read_csv('E:/Procesos Sense/Rentabilidad/RentTotalPBI_Prueba.txt')
##print(Base_Rent.columns)
Base_Rent = Base_Rent.drop(['Area', 'Tipo de Venta', 'Tipo_ResortFee', 'Registry',
       'Comercializadora', 'ContractNumber',
       'ReservationSubTypeNew', 'ReservationTypeNew', 'FirstNight',
       'LastNight', 'Mix_Mercado', 'Mix_programa', 'Prospectable',
       'ReservationStatus', 'Mix_Cliente', 'DateCreated', 'Nights',
       'SiteGroup', 'RoomType', 'Wk_Mayan', 'Promotion', 'ExchangeMembership',
       'ID', 'Id_Prom_Cam', 'Tipo_C_P', 'No Show', 'Ident_Hook',
       'Clasificador_HK', 'Año_Mes', 'Año', 'año_Llegada', 'mes_Llegada',
       'Monto de Venta', 'Venta', 'Reservacion',
       'Plaza', 'Año_Ventas', 'BRM', 'CM_Noches1',
       'Ingresos', 'Egresos', 'Benefit_SC', 'Uso_SC',
       'Exit', 'VolumenExit', 'ComExit',
       'AjusteSC', 'Paq_Admvo_Dolares', 
       'Tipo de Canal', 'EstatusInnsist', 'SiteName', 'Campaign',
       'PromotionCode', 'Actualización', 'Tipo Salto', 'Categoria', 'Unidad',
       'Roomtype_Orig', 'Total_Saltos', 'Clasificación RF', 'Usage_Type',
       'Clasificación_Members', 'Equity_USD', 'Intervalo', '%MemberID'], axis=1)
print(Base_Rent.columns)
print(np.unique(list(Base_Rent['Mix_NA_IN'])))

Base_Rent_INT= Base_Rent[Base_Rent['Mix_NA_IN']=='IN']
Base_Rent_NAT= Base_Rent[Base_Rent['Mix_NA_IN']!='IN']
print('prueba')


Base_Rent_INT.to_csv(path+'/BaseDatos/Base_Trabajo_INT.csv',index=False)
Base_Rent_NAT.to_csv(path+'/BaseDatos/Base_Trabajo_NAT.csv',index=False)
