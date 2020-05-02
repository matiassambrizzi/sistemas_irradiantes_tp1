#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 18:39:25 2020
@author: matias
Srcipt para realizar el trabajo practico numero 1 de la materia Sistemas Irradiantes FIUBA

Numpy define el tipo de dato ndarray que es una coleccion de datos del mismo tipo
"""
import numpy as np
"""
@brief funcion principal
"""
def main():
    s = np.genfromtxt('../ArchivosDeMedicion/ArchivosS1p/AutoSave1.s1p' \
                      ,delimiter='\t',skip_header=8,usecols=(0,1,2));
    

if __name__ == '__main__':
    main()