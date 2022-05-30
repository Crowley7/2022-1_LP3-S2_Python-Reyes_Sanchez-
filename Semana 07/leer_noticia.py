# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:33:10 2022

@author: admin
"""

noticia = open("noticia.txt","rt",encoding=('utf8'))
datos_noticia = noticia.read()
print(datos_noticia)