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
@brief funcion para leer data de un archivo
@param location es la ubicacion del archivo
@param cols tupla que indica las columnas que se quieren leer
@param delim es el delimitador
@return s los datos leidos
"""
def readData(location,cols,delim):
    s = np.genfromtxt(location \
                      ,delimiter=delim,skip_header=8,usecols=cols);
    return s;

"""
@brief transformar un array de dos dimensiones a un numero complejo \
    input = [Re,Im]
@return lista de numeros complejos
"""
def arrayToComplex(arr,real,imag):
    return list(map(lambda x: x[real] + x[imag]*1j,arr));

"""
@brief
"""
def reflexionToImpedance(arr,zo):
    return list(map(lambda  x: zo * (1 + x) / (1 - x),arr));
"""
@brief funcion principal
"""
def main():
    
    zo = 50;
    data = readData('../ArchivosDeMedicion/ArchivosS1p/AutoSave1.s1p',(0,1,2),'\t');
    #Transform data to complex number    
    s11 = arrayToComplex(data,1,2)
    #Transfomr reflexion to impedance
    z = reflexionToImpedance(s11,zo);
    
    plt.figure(figsize=(8,8));
    SmithAxes.update_scParams(axes_impedance = 50);
    plt.subplot(1,1,1, projection='smith',grid_major_enable=True);
    plt.plot(z, datatype=SmithAxes.Z_PARAMETER)
    #leg = plt.legend(loc="lower right", fontsize=12)
    plt.show()
    
if __name__ == '__main__':
    main();
    
    
"""
TODO: carta de smith
plt.figure(figsize=(8,8)) 
SmithAxes.update_scParams(axes_impedance = 75)
plt.subplot(1,1,1, projection='smith',grid_major_enable=True) 
plt.plot(zl+0j , label="50+50j", datatype=SmithAxes.Z_PARAMETER)
leg = plt.legend(loc="lower right", fontsize=12)
plt.show()
"""