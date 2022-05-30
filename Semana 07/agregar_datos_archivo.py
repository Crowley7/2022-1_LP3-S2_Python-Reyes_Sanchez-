# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:48:50 2022

@author: admin
"""

archivo = open("noticia.txt","at")
#\n es para agregar el contenido en una línea al final

contenido = "\nFuente: RPP"

archivo.write(contenido)

archivo.close()

