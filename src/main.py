#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Sat May  2 18:39:25 2020
@author: matias
Srcipt para realizar el trabajo practico numero 1 de la materia Sistemas Irradiantes FIUBA

Numpy define el tipo de dato ndarray que es una coleccion de datos del mismo tipo
"""
from pathlib import Path #TODO: ver
from smithplot import SmithAxes
import numpy as np
import matplotlib.pyplot as plt



WORKING_DIR = Path.cwd()

IMG_DIR = "imagenes"
SRC_DIR = "src/"
IMG_TYPE = "png"
S1P_DATA_DIR = "ArchivosDeMedicion/ArchivosS1p/"
S2P_DATA_DIR = "ArchivosDeMedicion/ArchivosS2p/"

"""@brief funcion para leer data de un archivo
@param location es la ubicacion del archivo
@param cols tupla que indica las columnas que se quieren leer
@param delim es el delimitador
@return s los datos leidos
"""

def read_data(location, cols, delim):
    data = np.genfromtxt(location,
                         delimiter=delim, skip_header=8, usecols=cols)
    return data

"""@brief transformar un array de dos dimensiones a un numero complejo \
    input = [Re,Im]
@return lista de numeros complejos
"""
def array_to_complex(arr, real, imag):
    return [x[real] + x[imag]*1j for x in arr]

"""@brief transformar los coeficiente de reflexion en impedancia para poder \
    plotear en la carta de smith
"""
def reflexion_coefficient_to_impedance(arr, caracteristic_impedance):
    return [caracteristic_impedance * (1+x)/(1-x) for x in arr]

"""@brief plot smith chart function
"""
def plot_smith_chart(input_impedance, caracteristic_impedance, file_name):
    directory = WORKING_DIR.parent / IMG_DIR
    if directory.is_dir() == False:
        directory.mkdir()
    fig = plt.figure(figsize=(10, 8))
    SmithAxes.update_scParams(axes_impedance=caracteristic_impedance)
    plt.subplot(1, 1, 1, projection='smith', grid_major_enable=True)
    plt.plot(input_impedance, datatype=SmithAxes.Z_PARAMETER)
    plt.show()
    fig.savefig(directory / f'{file_name}.{IMG_TYPE}',\
                bbox_inches='tight', dpi=150)
"""@brief funcion principal
"""
def main():
    caracteristic_impedance: int = 50
    #TODO: tratar de manejar todo usando Path()
    s1p_file_dir = WORKING_DIR.parent / S1P_DATA_DIR
    #Uso un generador, esto me ahorra memoria porque no crea una lista
    #Una vez que uso el gnerador ya no lo puedo volver a usar
    s1p_files = (s1p_file_dir / f'AutoSave{n}.s1p' for n in range(1, 10));
    #Ploteo la carta de smith para todos los archivos
    for file in s1p_files:
        print('Ploteando', file.stem)
        data = read_data(file,
                         (0, 1, 2), '\t')
        s_11_parameter = array_to_complex(data, 1, 2)
        input_impedance = reflexion_coefficient_to_impedance(s_11_parameter,
                                                             caracteristic_impedance)
        plot_smith_chart(input_impedance, caracteristic_impedance,
                         file.name)

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