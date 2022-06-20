# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 09:06:28 2022

@author: admin
"""

import sqlite3

conexion = sqlite3.connect("bdbiblioteca.db")

consulta = """ INSERT INTO
                pais (nombre, estado)
                VALUES('BRASIL','A')
            """

cursor = conexion.cursor()
cursor.execute(consulta)
conexion.commit()

