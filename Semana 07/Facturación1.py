# -*- coding: utf-8 -*-
"""
Created on Mon May 30 09:17:26 2022

@author: admin
"""

import financieros
subtotal=800.77

print(f"Subtotal: {subtotal}")
print(f"IGV: {financieros.obtenerIGVconSubtotal(subtotal): .2}")
print(f"Total: {financieros.obtenerTotalconSubtotal(subtotal): .2}")
