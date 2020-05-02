#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 18:39:25 2020
@author: matias
Srcipt para realizar el trabajo practico numero 1 de la materia Sistemas Irradiantes FIUBA

Numpy define el tipo de dato ndarray que es una coleccion de datos del mismo tipo
"""
import numpy as np
import matplotlib.pyplot as plt
from smithplot import SmithAxes 
from smithplot import smithhelper
"""
@brief funcion principal
"""
def main():
    
    zo = 50;
    s = np.genfromtxt('../ArchivosDeMedicion/ArchivosS1p/AutoSave1.s1p' \
                      ,delimiter='\t',skip_header=8,usecols=(0,1,2));
    
    complexNumbers = [];
    freq = [];
    
    for elements in s:
        complexNumbers.append(elements[1] + elements[2]*1j);
        freq.append(elements[0]);
    
    z = [];
    for c in complexNumbers:
        z.append(zo * (1 + c) / (1 - c));
        
    plt.figure(figsize=(8,8)) 
    SmithAxes.update_scParams(axes_impedance = 50)
    plt.subplot(1,1,1, projection='smith',grid_major_enable=True) 
    plt.plot(z, datatype=SmithAxes.Z_PARAMETER)
    #leg = plt.legend(loc="lower right", fontsize=12)
    plt.show()
    
if __name__ == '__main__':
    main()
    
    
"""
TODO: carta de smith
plt.figure(figsize=(8,8)) 
SmithAxes.update_scParams(axes_impedance = 75)
plt.subplot(1,1,1, projection='smith',grid_major_enable=True) 
plt.plot(zl+0j , label="50+50j", datatype=SmithAxes.Z_PARAMETER)
leg = plt.legend(loc="lower right", fontsize=12)
plt.show()
"""