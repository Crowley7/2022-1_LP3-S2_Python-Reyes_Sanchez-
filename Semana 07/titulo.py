# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:04:56 2022

@author: admin
"""

# Importamos la libreria 

import camelcase

nombre = "Oscar Elias Reyes Sanchez"
print(nombre.upper())
print(nombre.title())

#Creamos un objeto llamado cam
cam = camelcase.CamelCase()
print("Con camelcase.....")

#Imprimimos el nombre en formato titulo
#Utilizamos camelcase

print(cam.hump(nombre))

#Para resolver el problema
# Creamos otro objeto llamado cam2
# Al definir el objeto, incluimos los argumentos
# 'Oscar' y  'Reyes'

cam2=camelcase.CamelCase('Oscar','Reyes')
print(cam2.hump(nombre))