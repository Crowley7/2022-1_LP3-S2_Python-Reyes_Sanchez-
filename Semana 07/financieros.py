# -*- coding: utf-8 -*-
"""
Created on Mon May 30 08:57:42 2022

@author: admin
Los Módulos te permitirán crear librerías de funcionalidades que puedas
utilizar o reutilizar en cualquier momento en tu proyecto.
"""


igv = 0.18

def obtenerIGVconSubtotal(subtotal):
    return subtotal*igv

def obtenerTotalconSubtotal(subtotal):
    # subtotal + igv*subtotal
    # subtotal*(1+0.18)
    return subtotal*(1+igv)

def obtenerSubtotalconTotal(total):
    return total/(1+igv)

def obtenerIGVconTotal(total):
    return total-obtenerSubtotalconTotal(total)
