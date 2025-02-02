#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 12:41:30 2022

@author: ignacioacuna
"""
import pandas as pd
from datetime import datetime
import os.path
import os
from dotenv import load_dotenv
load_dotenv()

BASE_URL = os.getenv('BASE_URL')

###################################
#            CEAZA                #
###################################


datasets = ["direccion_viento_ceaza", "presion_ceaza", "velocidad_viento_ceaza",
            "temperatura_suelo_ceaza", "temperatura_aire_ceaza", "radiacion_ceaza", 
            "precipitacion_ceaza", "pto_rocio_ceaza","humedad_relativa_ceaza", "evotranspiracion_ceaza"]


for ds in datasets:
    if(not os.path.isdir('../output/'  + ds) ) :
        os.mkdir('../output/'  + ds)
    # Leemos los archivos directamente desde el servidor del Observatorio de Cambio Climático
    url = BASE_URL + ds + "/" + ds +".csv"
    print("Reading file:", ds)
    print("URL:", url)
    df = pd.read_csv(url,  dtype={'latitud': float,'longitud': float, 'statusCode': float, 'nombre': object }, parse_dates=["time"])
    
    # Obtenemos los valores temporales para genera los sub conjuntos anuales, con tal de dividir el dataset en pedazos ('chunks') más pequeños
    # y así poder subir al repositorio (debido a capacidad máxima de 100Mb por repo)
    t_minimo =  datetime.utcfromtimestamp(pd.to_datetime(df["time"].min()).value / 1000000000).strftime("%Y")
    t_maximo =  datetime.utcfromtimestamp(pd.to_datetime(df["time"].max()).value / 1000000000).strftime("%Y")
    
    for i in range(int(t_minimo), int(t_maximo)  + 1):
        print("Cortando desde", i, i+1)
        temp = df.loc[(df['time'] > str(i) + '-1-1') & (df['time'] <=  str(i + 1) + '-1-1'), ]
        
        # Si no existen las carpetas de los años, se crean
        if(not os.path.isdir('../output/' + ds + "/" + str(i)) ):
            os.mkdir('../output/' + ds + "/" + str(i)  ) 
        
        # Se guarda el archivo temporal en la carpeta correspondiente
        temp.to_csv('../output/' + ds + "/" + str(i) + "/" + str(i) + "_" + ds  + ".csv", index = False )
        
        
###################################
#            DMC                  #
###################################

datasets = ["agua24_dmc", "agua6_dmc", "humedad_dmc",
            "presionqfe_dmc", "presionqff_dmc", "tminima_dmc", 
            "tmaxima_dmc", "rocio_dmc","temperatura_dmc", "viento_dmc"] 
    
for ds in datasets:
    if(not os.path.isdir('../output/'  + ds) ) :
        os.mkdir('../output/'  + ds)
    # Leemos los archivos directamente desde el servidor del Observatorio de Cambio Climático
    url = BASE_URL + ds + "/" + ds +".csv"
    print("Reading file:", ds)
    print("URL:", url)
    df = pd.read_csv(url,  dtype={'latitud': float,'longitud': float, 'CodigoNacional': float, 'nombreEstacion': object }, parse_dates=["time"])
    
    # Obtenemos los valores temporales para genera los sub conjuntos anuales, con tal de dividir el dataset en pedazos ('chunks') más pequeños
    # y así poder subir al repositorio (debido a capacidad máxima de 100Mb por repo)
    t_minimo =  datetime.utcfromtimestamp(pd.to_datetime(df["time"].min()).value / 1000000000).strftime("%Y")
    t_maximo =  datetime.utcfromtimestamp(pd.to_datetime(df["time"].max()).value / 1000000000).strftime("%Y")
    
    for i in range(int(t_minimo), int(t_maximo)  + 1):
        print("Cortando desde", i, i+1)
        temp = df.loc[(df['time'] > str(i) + '-1-1') & (df['time'] <=  str(i + 1) + '-1-1'), ]
        
        # Si no existen las carpetas de los años, se crean
        if(not os.path.isdir('../output/' + ds + "/" + str(i)) ):
            os.mkdir('../output/' + ds + "/" + str(i)  ) 
        
        # Se guarda el archivo temporal en la carpeta correspondiente
        temp.to_csv('../output/' + ds + "/" + str(i) + "/" + str(i) + "_" + ds  + ".csv", index = False )
    
    
    
    
###################################
#            SINCA                #
###################################

datasets = ["co_sinca", "no2_sinca", "o3_sinca",
            "so2_sinca", "humedad_sinca", "mpm10_sinca", 
            "mpm25_sinca", "precipitaciones_sinca","presion_sinca"] 


for ds in datasets:
    if(not os.path.isdir('../output/'  + ds) ) :
        os.mkdir('../output/'  + ds)
    # Leemos los archivos directamente desde el servidor del Observatorio de Cambio Climático
    url = BASE_URL + ds + "/" + ds +".csv"
    print("Reading file:", ds)
    print("URL:", url)
    df = pd.read_csv(url,  dtype={'latitud': float,'longitud': float, 'codigoEstacion': object, 'nombreEstacion': object }, parse_dates=["time"])
    
    # Obtenemos los valores temporales para genera los sub conjuntos anuales, con tal de dividir el dataset en pedazos ('chunks') más pequeños
    # y así poder subir al repositorio (debido a capacidad máxima de 100Mb por repo)
    t_minimo =  datetime.utcfromtimestamp(pd.to_datetime(df["time"].min()).value / 1000000000).strftime("%Y")
    t_maximo =  datetime.utcfromtimestamp(pd.to_datetime(df["time"].max()).value / 1000000000).strftime("%Y")
    
    for i in range(int(t_minimo), int(t_maximo)  + 1):
        print("Cortando desde", i, i+1)
        temp = df.loc[(df['time'] > str(i) + '-1-1') & (df['time'] <=  str(i + 1) + '-1-1'), ]
        
        # Si no existen las carpetas de los años, se crean
        if(not os.path.isdir('../output/' + ds + "/" + str(i)) ):
            os.mkdir('../output/' + ds + "/" + str(i)  ) 
        
        # Se guarda el archivo temporal en la carpeta correspondiente
        temp.to_csv('../output/' + ds + "/" + str(i) + "/" + str(i) + "_" + ds  + ".csv", index = False ) 
