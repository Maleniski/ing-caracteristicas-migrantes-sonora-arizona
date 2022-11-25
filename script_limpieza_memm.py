"""
Universidad de Sonora
Maestría en Ciencia de Datos

Asignatura: Ingeniería de Características
Docente: Doctor Julio Waissman Vilanova
Alumno: María Elena Martínez Manzanares

Fecha: 25 de noviembre del 2022

Descripción: En el siguiente script de python es parte del proyecto final del curso de Ingeniería de 
características. El objeto del proyecto es, por medio de datos, describir que le ocurre a un inmigrante
ilegal cruzando la frontera Sonora Arizona cuando es capturado o encontrado por oficiales estadounidenses.

Los datos se originan de dos fuentes, el Arizona OpenGIS Initiative for Deceased Migrants y la SEGOB.

El script baja los archivos de la fuente, armoniza las variables y da tratamiento a los datos perdidos.

El script concluye con la generación de un solo archivo csv donde se incluye toda esta información. 

La documentación y archivos que componene la totalidad del proyecto se encuentra disponible en el
siguiente repositorio de GitHub: bit.ly/PF_IngCaract_Manzanares .

Este proyecto tiene una página de GitHub que usted puede revisar para más información disponible 
en la siguiente liga: https://bit.ly/MigrantsArizonaSonora_Manzanares .

Observación.
La armonización de las variables puede ser un proceso tardado dependiendo de su equipo.
"""

import pandas as pd
import numpy as np
import datetime
import urllib.request
import os
from zipfile import ZipFile
import wget


#Si desea cambiar donde se descargaran los datos, modificar la siguiente variable.

subdir = "./"

#---------------Descarga de datos desde su fuente-------------------#
print("#---------------Descarga de datos desde su fuente-------------------#")

#URL datos de la SEGOB
SEGOB_2021='http://portales.segob.gob.mx/work/models/PoliticaMigratoria/CEM/Estadisticas/BDatos/DevMexEUU/DwnldBD.php?f=BDSIOMR_PUB_2021_UPMRIP.csv'
SEGOB_2020='http://portales.segob.gob.mx/work/models/PoliticaMigratoria/CEM/Estadisticas/BDatos/DevMexEUU/DwnldBD.php?f=BDSIOMR_PUB_2020_UPMRIP.csv'
SEGOB_2019='http://portales.segob.gob.mx/work/models/PoliticaMigratoria/CEM/Estadisticas/BDatos/DevMexEUU/DwnldBD.php?f=BDSIOMR_PUB_2019_UPMRIP.csv'
SEGOB_2018='http://portales.segob.gob.mx/work/models/PoliticaMigratoria/CEM/Estadisticas/BDatos/DevMexEUU/DwnldBD.php?f=BDSIOMR_PUB_2018_UPMRIP.csv'
SEGOB_2017='http://portales.segob.gob.mx/work/models/PoliticaMigratoria/CEM/Estadisticas/BDatos/DevMexEUU/DwnldBD.php?f=BDSIOMR_PUB_2017_UPMRIP.csv'
SEGOB_2016='http://portales.segob.gob.mx/work/models/PoliticaMigratoria/CEM/Estadisticas/BDatos/DevMexEUU/DwnldBD.php?f=BDSIOMR_PUB_2016_UPMRIP.csv'
Catalogos_SEGOB='http://portales.segob.gob.mx/work/models/PoliticaMigratoria/CEM/Estadisticas/BDatos/DevMexEUU/CatRepatriados_2021.xls'

#Ubicacion para datos de la SEGOB
SEGOB_2021_archivo='BDSIOMR_PUB_2021_UPMRIP.csv'
SEGOB_2020_archivo='BDSIOMR_PUB_2020_UPMRIP.csv'
SEGOB_2019_archivo='BDSIOMR_PUB_2019_UPMRIP.csv'
SEGOB_2018_archivo='BDSIOMR_PUB_2018_UPMRIP.csv'
SEGOB_2017_archivo='BDSIOMR_PUB_2017_UPMRIP.csv'
SEGOB_2016_archivo='BDSIOMR_PUB_2016_UPMRIP.csv'
Catalogos_SEGOB_archivo="Catalogo_SEGOB.xls"

#URL datos del Arizona OpenGIS Initiative for Deceased Migrants
ARIZONA_DM='https://humaneborders.info/app/getTableByMultipleSearch.asp?sex=&cod=&county=&corridors=&sm=&years=&name=&detail=full&format=csv'

#Ubicacion para datos del DM
ARIZONA_DM_archivo='DM.csv'

SEGOB = { SEGOB_2021:SEGOB_2021_archivo, SEGOB_2020:SEGOB_2020_archivo, 
        SEGOB_2019:SEGOB_2019_archivo, SEGOB_2018:SEGOB_2018_archivo, 
        SEGOB_2017:SEGOB_2017_archivo, SEGOB_2016:SEGOB_2016_archivo,
         Catalogos_SEGOB: Catalogos_SEGOB_archivo}
ARIZONA = { ARIZONA_DM:ARIZONA_DM_archivo }         

for url, archivo in SEGOB.items(): 
    if not os.path.exists(archivo):
        if not os.path.exists(subdir):
            os.makedirs(subdir)
        urllib.request.urlretrieve(url, subdir + archivo)
print("Descarga de SEGOB terminada.")

for url, archivo in ARIZONA.items(): 
    if not os.path.exists(archivo):
        if not os.path.exists(subdir):
            os.makedirs(subdir)
        urllib.request.urlretrieve(url, subdir + archivo)
print("Descarga de Arizona OpenGIS Initiative for Deceased Migrants.") 

#---------------Log de la descarga-------------------#
print("#---------------Creando LOG de la descarga-------------------#")

with open(subdir + "info.txt", 'w') as f:
    f.write("Archivos con datos de migrantes localizados en frontera Sonora-Arizona. \n")
    info = """
    Los datos fueron descargados de los portales de la SEGOB y el Arizona OpenGIS Initiative for Deceased Migrants. 
    El Arizona OpenGIS Initiative for Deceased Migrants presentan datos  relacionados de muertes de migrantes tratando 
    de cruzar la frontera Sonora-Estados Unidos y los datos provistos por la SEGOB presentan información de repatriados 
    desde Estados Unidos a México.

    """ 
    f.write(info + '\n')
    f.write("Descargado el " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    f.write("|-------------------------Metadatos de la descarga de la SEGOB-------------------------|"+'\n')    
    for url, archivo in SEGOB.items():        
        f.write("Desde: " + url + "\n")
        f.write("Nombre: " + archivo + "\n")            
    f.write("|-------------Metadatos de la descarga del Arizona OpenGIS Initiative for Deceased Migrants------------|"+'\n') 
    for url, archivo in ARIZONA.items():        
        f.write("Desde: " + url + "\n")
        f.write("Nombre: " + archivo + "\n")  


#---------------Integración de datos de cada fuente en dos fuentes (1 de Arizona y 1 SEGOB)-------------------#
print("#---------------Integración de datos de cada fuente en dos fuentes (1 de Arizona y 1 SEGOB)-------------------#")

arizona=pd.read_csv("data//"+ARIZONA_DM_archivo)

arizona_columns=['Name', 
                'Sex', 
                'Age', 
                'Reporting Date',
                'Cause of Death',
                'OME Determined COD',
                'Body Condition',
                'Post Mortem Interval',  
                'County']

ARIZONA_tidy=arizona[arizona_columns].copy()
ARIZONA_tidy['Reporting Date'] = ARIZONA_tidy['Reporting Date'].astype('datetime64[ns]')
ARIZONA_tidy['Age'] = ARIZONA_tidy['Age'].astype('Int64')

SEGOB1=pd.read_csv("data//BDSIOMR_PUB_2016_UPMRIP.csv")
#Registros que estan relacionados con Sonora o la frontera con Sonora.
SEGOB1=SEGOB1[ (SEGOB1["DEL"]==26) | #Entidad federativa donde se ubica el punto de repatriación (Sonora)
        (SEGOB1["EDO_DET"]==4) ] #Estado de la Unión Americana donde la persona repatriada declaró haber sido detenido. (Arizona)

SEGOB2=pd.read_csv("data//BDSIOMR_PUB_2017_UPMRIP.csv")
#Registros que estan relacionados con Sonora o la frontera con Sonora.
SEGOB2=SEGOB2[ (SEGOB2["DEL"]==26) | #Entidad federativa donde se ubica el punto de repatriación (Sonora)
        (SEGOB2["EDO_DET"]==4) ] #Estado de la Unión Americana donde la persona repatriada declaró haber sido detenido. (Arizona)

SEGOB3=pd.read_csv("data//BDSIOMR_PUB_2018_UPMRIP.csv")
#Registros que estan relacionados con Sonora o la frontera con Sonora.
SEGOB3=SEGOB3[ (SEGOB3["DEL"]==26) | #Entidad federativa donde se ubica el punto de repatriación (Sonora)
        (SEGOB3["EDO_DET"]==4) ] #Estado de la Unión Americana donde la persona repatriada declaró haber sido detenido. (Arizona)

SEGOB4=pd.read_csv("data//BDSIOMR_PUB_2019_UPMRIP.csv")
#Registros que estan relacionados con Sonora o la frontera con Sonora.
SEGOB4=SEGOB4[ (SEGOB4["DEL"]==26) | #Entidad federativa donde se ubica el punto de repatriación (Sonora)
        (SEGOB4["EDO_DET"]==4) ] #Estado de la Unión Americana donde la persona repatriada declaró haber sido detenido. (Arizona)

SEGOB5=pd.read_csv("data//BDSIOMR_PUB_2020_UPMRIP.csv")
#Registros que estan relacionados con Sonora o la frontera con Sonora.
SEGOB5=SEGOB5[ (SEGOB4["DEL"]==26) | #Entidad federativa donde se ubica el punto de repatriación (Sonora)
        (SEGOB5["EDO_DET"]==4) ] #Estado de la Unión Americana donde la persona repatriada declaró haber sido detenido. (Arizona)


SEGOB6=pd.read_csv("data//BDSIOMR_PUB_2021_UPMRIP.csv")
#Registros que estan relacionados con Sonora o la frontera con Sonora.
SEGOB6=SEGOB6[ (SEGOB6["DEL"]==26) | #Entidad federativa donde se ubica el punto de repatriación (Sonora)
        (SEGOB6["EDO_DET"]==4) ] #Estado de la Unión Americana donde la persona repatriada declaró haber sido detenido. (Arizona)

SEGOB_tidy=pd.concat([SEGOB1, SEGOB2, SEGOB3, SEGOB4, SEGOB5, SEGOB6])
SEGOB_tidy.drop(["IER","PUNT_REP"],axis=1,inplace=True)
SEGOB_tidy['FEC_REP'] = SEGOB_tidy['FEC_REP'].astype('datetime64[ns]')

#Leemos primer catalogo
variables = pd.read_excel("data//"+Catalogos_SEGOB_archivo, index_col=0, sheet_name='Variables')
variables.reset_index(drop=True, inplace=True)

#La siguiente linea de código es para quitar el multiindex que tiene la tabla con los catalogos.
variables["Nombre de la variable"]=variables["Nombre de la variable"].fillna(method='ffill')


#-------------------Decodificacion de datos de la SEGOB------------------------#
print("#-------------------Decodificacion de datos de la SEGOB------------------------#")

#Con un ciclo for realizaremos el left merge. Esto lo podemos hacer con todas las columnas que hay que parsear con excepción de "MUN_DES" y "MUN_NAC" 
#que tienen sus propios catalogos y realizaremos el merge aparte.
caracteristicas=SEGOB_tidy.columns.tolist()
caracteristicas.remove('MUN_DES')
caracteristicas.remove('MUN_NAC')

#Realizaremos el merge sobre una copia de la tidy data
SEGOB_tidy_V2=SEGOB_tidy.copy()

for caracteristica in caracteristicas:
    right=variables[variables["Nombre de la variable"]==caracteristica]
    right.rename(columns={ "Valor" : caracteristica, 'Etiqueta' : caracteristica +'_parsed' }, inplace=True)
    right.drop(["Observaciones","Nombre de la variable"], axis=1, inplace=True)

    SEGOB_tidy_V2 = pd.merge(SEGOB_tidy_V2, right, how='left', on=caracteristica)

#Nos falta catalogo "MUN_NAC" y "MUN_DES". Hacemos este último tratamiento a continuación.

mun_nac = pd.read_excel("data//"+Catalogos_SEGOB_archivo, index_col=0, sheet_name='MUN_NAC')
mun_nac.reset_index(drop=True, inplace=True)
mun_des = pd.read_excel("data//"+Catalogos_SEGOB_archivo, index_col=0, sheet_name='MUN_DES')
mun_des.reset_index(drop=True, inplace=True)

for caracteristica in "MUN_NAC", "MUN_DES":
    if(caracteristica == "MUN_NAC"):
        right=mun_nac.copy()
    else:
        right=mun_des.copy()

    right.drop([caracteristica], axis=1, inplace=True)
    right.rename(columns={ "Valor" : caracteristica, 'Etiqueta' : caracteristica +'_parsed' }, inplace=True)

    SEGOB_tidy_V2 = pd.merge(SEGOB_tidy_V2, right, how='left', on=caracteristica)

#--------------------Manejo de valores perdidos-----------------#
print("#--------------------Manejo de valores perdidos-----------------#")

ARIZONA_tidy["Sex"].fillna("undetermined", inplace = True)
ARIZONA_tidy["Age"].fillna(-1, inplace = True)
ARIZONA_tidy["Cause of Death"].fillna("undetermined", inplace = True)
ARIZONA_tidy["OME Determined COD"].fillna("undetermined", inplace = True)
ARIZONA_tidy["Body Condition"].fillna("undetermined", inplace = True)
ARIZONA_tidy["Post Mortem Interval"].fillna("undetermined", inplace = True)

SEGOB_tidy_V3 = SEGOB_tidy_V2[['DEL_parsed', 'FEC_REP', 'CLASIF_REP_parsed', 'SEXO_parsed', 'EDA', 'EN_NAC_parsed',
       'NIV_ESC_parsed', 'ACOM_REP_parsed', 'PERM_EU_parsed', 'EDO_DET_parsed',
       'AUT_DEP_parsed', 'EN_DES_parsed', 'CAN_AL_parsed', 'CAN_COM_parsed',
       'CAN_DIF_parsed', 'CAN_HOS_parsed', 'CAN_STRA_parsed',
       'CAN_SEGPOP_parsed', 'CAN_OFAM_parsed', 'AGUA_AL_parsed',
       'DESC_BUS_parsed', 'APO_AUX_parsed', 'APO_LLAM_parsed',
       'APO_MAT_parsed', 'APO_TRAS_parsed', 'APO_VES_parsed',
       'APO_ACT_NAC_parsed', 'APO_TRASF_parsed', 'APO_CURP_parsed',
       'APO_ASF_parsed', 'APO_AME_parsed', 'APO_REC_PERT_parsed',
       'APO_AT_MEDICA_parsed']].copy()

SEGOB_tidy_V3.drop(['APO_TRASF_parsed'], axis=1, inplace=True)
SEGOB_tidy_V3[SEGOB_tidy_V3.isna().any(axis=1)].sort_values(by=['FEC_REP'])
SEGOB_tidy_V3["APO_CURP_parsed"].fillna("Sin determinar", inplace = True)
SEGOB_tidy_V3["APO_ASF_parsed"].fillna("Sin determinar", inplace = True)
SEGOB_tidy_V3["APO_AME_parsed"].fillna("Sin determinar", inplace = True)
SEGOB_tidy_V3["APO_REC_PERT_parsed"].fillna("Sin determinar", inplace = True)
SEGOB_tidy_V3["APO_AT_MEDICA_parsed"].fillna("Sin determinar", inplace = True)

#------------------------Armonización de variables-------------------------#
print("#------------------------Armonización de variables-------------------------#")

ARIZONA_tidy=ARIZONA_tidy[(ARIZONA_tidy["Reporting Date"]>="2016-01-01") & (ARIZONA_tidy["Reporting Date"]<="2021-12-31")]
harmonized_data = pd.DataFrame(columns = ["VIVO", "NOMBRE", "SEXO", "EDAD", "FECHA",
                                          'DEL', 'CLASIF_REP', 'EN_NAC',
                                          'NIV_ESC', 'ACOM_REP', 'PERM_EU', 'EDO_DET',
                                          'AUT_DEP', 'EN_DES', 'CAN_AL', 'CAN_COM',
                                          'CAN_DIF', 'CAN_HOS', 'CAN_STRA',
                                          'CAN_SEGPOP', 'CAN_OFAM', 'AGUA_AL',
                                          'DESC_BUS', 'APO_AUX', 'APO_LLAM',
                                          'APO_MAT', 'APO_TRAS', 'APO_VES',
                                          'APO_ACT_NAC', 'APO_CURP','APO_ASF', 
                                          'APO_AME', 'APO_REC_PERT',
                                          'APO_AT_MEDICA', "CAUSA_MUERTE","OME_CAUSA_MUERTE",
                                          "CONDICION_CUERPO","INTERVALO_POST_MORTEM","COUNTY"])

for registro in range(SEGOB_tidy_V3.shape[0]):
    harmonized_data = pd.concat([harmonized_data, pd.DataFrame.
                        from_records([{"VIVO":"Si",
                                        "NOMBRE":"No aplica",
                                        "SEXO": SEGOB_tidy_V3["SEXO_parsed"].iloc[registro], 
                                        "EDAD": SEGOB_tidy_V3["EDA"].iloc[registro], 
                                        "FECHA": SEGOB_tidy_V3["FEC_REP"].iloc[registro],
                                        'DEL':SEGOB_tidy_V3["DEL_parsed"].iloc[registro], 
                                        'CLASIF_REP': SEGOB_tidy_V3["CLASIF_REP_parsed"].iloc[registro],
                                        'EN_NAC': SEGOB_tidy_V3["EN_NAC_parsed"].iloc[registro],
                                        'NIV_ESC': SEGOB_tidy_V3["NIV_ESC_parsed"].iloc[registro], 
                                        'ACOM_REP': SEGOB_tidy_V3["ACOM_REP_parsed"].iloc[registro], 
                                        'PERM_EU': SEGOB_tidy_V3["PERM_EU_parsed"].iloc[registro], 
                                        'EDO_DET': SEGOB_tidy_V3["EDO_DET_parsed"].iloc[registro],
                                        'AUT_DEP': SEGOB_tidy_V3["AUT_DEP_parsed"].iloc[registro], 
                                        'EN_DES': SEGOB_tidy_V3["EN_DES_parsed"].iloc[registro], 
                                        'CAN_AL': SEGOB_tidy_V3["CAN_AL_parsed"].iloc[registro], 
                                        'CAN_COM': SEGOB_tidy_V3["CAN_COM_parsed"].iloc[registro],
                                        'CAN_DIF': SEGOB_tidy_V3["CAN_DIF_parsed"].iloc[registro], 
                                        'CAN_HOS': SEGOB_tidy_V3["CAN_HOS_parsed"].iloc[registro], 
                                        'CAN_STRA': SEGOB_tidy_V3["CAN_STRA_parsed"].iloc[registro],
                                        'CAN_SEGPOP': SEGOB_tidy_V3["CAN_SEGPOP_parsed"].iloc[registro], 
                                        'CAN_OFAM': SEGOB_tidy_V3["CAN_OFAM_parsed"].iloc[registro], 
                                        'AGUA_AL': SEGOB_tidy_V3["AGUA_AL_parsed"].iloc[registro],
                                        'DESC_BUS': SEGOB_tidy_V3["DESC_BUS_parsed"].iloc[registro], 
                                        'APO_AUX': SEGOB_tidy_V3["APO_AUX_parsed"].iloc[registro], 
                                        'APO_LLAM': SEGOB_tidy_V3["APO_LLAM_parsed"].iloc[registro],
                                        'APO_MAT': SEGOB_tidy_V3["APO_MAT_parsed"].iloc[registro], 
                                        'APO_TRAS': SEGOB_tidy_V3["APO_TRAS_parsed"].iloc[registro], 
                                        'APO_VES': SEGOB_tidy_V3["APO_VES_parsed"].iloc[registro],
                                        'APO_ACT_NAC': SEGOB_tidy_V3["APO_ACT_NAC_parsed"].iloc[registro], 
                                        'APO_CURP': SEGOB_tidy_V3["APO_CURP_parsed"].iloc[registro],
                                        'APO_ASF': SEGOB_tidy_V3["APO_ASF_parsed"].iloc[registro], 
                                        'APO_AME': SEGOB_tidy_V3["APO_AME_parsed"].iloc[registro], 
                                        'APO_REC_PERT': SEGOB_tidy_V3["APO_REC_PERT_parsed"].iloc[registro],
                                        'APO_AT_MEDICA': SEGOB_tidy_V3["APO_AT_MEDICA_parsed"].iloc[registro], 
                                        "CAUSA_MUERTE":"No aplica",
                                        "OME_CAUSA_MUERTE":"No aplica",
                                        "CONDICION_CUERPO":"No aplica",
                                        "INTERVALO_POST_MORTEM":"No aplica",
                                        "COUNTY":"No aplica"}])], ignore_index=True) 

for registro in range(ARIZONA_tidy.shape[0]):
    #Esto lo hago porque quiero la tabla en la medida de lo posible en español.
    if(ARIZONA_tidy["Name"].iloc[registro]=="male"):
      sexo="Hombre"
    else:
      sexo="Mujer"

    harmonized_data = pd.concat([harmonized_data, pd.DataFrame.
                        from_records([{"VIVO":"No",
                                        "NOMBRE":ARIZONA_tidy["Name"].iloc[registro],
                                        "SEXO":sexo, 
                                        "EDAD":ARIZONA_tidy["Age"].iloc[registro], 
                                        "FECHA":ARIZONA_tidy["Reporting Date"].iloc[registro],
                                        'DEL':"No aplica", 
                                        'CLASIF_REP':"No aplica", 
                                        'EN_NAC':"No aplica",
                                        'NIV_ESC':"No aplica", 
                                        'ACOM_REP':"No aplica", 
                                        'PERM_EU':"No aplica", 
                                        'EDO_DET':"No aplica",
                                        'AUT_DEP':"No aplica", 
                                        'EN_DES':"No aplica", 
                                        'CAN_AL':"No aplica", 
                                        'CAN_COM':"No aplica",
                                        'CAN_DIF':"No aplica", 
                                        'CAN_HOS':"No aplica", 
                                        'CAN_STRA':"No aplica",
                                        'CAN_SEGPOP':"No aplica", 
                                        'CAN_OFAM':"No aplica", 
                                        'AGUA_AL':"No aplica",
                                        'DESC_BUS':"No aplica", 
                                        'APO_AUX':"No aplica", 
                                        'APO_LLAM':"No aplica",
                                        'APO_MAT':"No aplica", 
                                        'APO_TRAS':"No aplica", 
                                        'APO_VES':"No aplica",
                                        'APO_ACT_NAC':"No aplica", 
                                        'APO_CURP':"No aplica",
                                        'APO_ASF':"No aplica", 
                                        'APO_AME':"No aplica", 
                                        'APO_REC_PERT':"No aplica",
                                        'APO_AT_MEDICA':"No aplica", 
                                        "CAUSA_MUERTE":ARIZONA_tidy["Cause of Death"].iloc[registro],
                                        "OME_CAUSA_MUERTE":ARIZONA_tidy["OME Determined COD"].iloc[registro],
                                        "CONDICION_CUERPO":ARIZONA_tidy['Body Condition'].iloc[registro],
                                        "INTERVALO_POST_MORTEM":ARIZONA_tidy['Post Mortem Interval'].iloc[registro],
                                        "COUNTY":ARIZONA_tidy['County'].iloc[registro]}])], ignore_index=True) 

print("#-----------------------Proceso terminado, se crea archivo csv-----------------------#")
harmonized_data.to_csv("migrantsdata.csv")                                       