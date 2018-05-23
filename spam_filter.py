#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
$spam_filter.py
------------
Archivo para poder generar un filtro de spam utilizando el método de Naive Bayes,
en forma laplaciana. Esto es, cada palabra se considera un atributo, el cual puede tener
valores binarios (1 si se encuentra en el mail y 0 si no se encuentra en el mail.
Las clases tambien son binarias, 1 si son spam y 0 si no son spam.
Los datos ya vienen preprocesados de forma que
"""

__author__ = 'juliowaissman'

from random import randint
import nb
import naive_bayes

def carga_datos(file_datos, file_clases):

    datos = []
    lineas = open(file_datos, 'r').readlines()
    for linea in lineas:
        datos.append([int(val) for val in linea.strip().strip(',').split(',')])

    clinea = open(file_clases).readline()
    clases = [int(cl) for cl in clinea.split()]

    return datos, clases


def carga_vocabulario():
    palabras = open('vocab.txt', 'r').readlines()
    return [palabra.strip().split()[1] for palabra in palabras]


def ejemplo_datos():
    datos, clases = carga_datos('mails.data', 'mails.class')
    vocabulario = carga_vocabulario()

    print "Datos: ", len(datos), " con dimension: ", len(datos[0])
    print "Clases: ", len(clases)
    print "Vocabulario: ", len(vocabulario)

    print "Ejemplos de correos en los datos"
    print "--------------------------------\n"

    for _ in range(10):
        mail = randint(0, len(clases) - 1)
        print "\nPara el mail ", mail, " tenemos las palabras:\n\n"
        print [vocabulario[i] for i in range(len(vocabulario)) if datos[mail][i] == 1]
        print "\ny el mail ", "es spam" if clases[mail] == 1 else "no es spam"
        print"\n-----------------------------------------------------------------------------------------------"


def spam_filter():
    """
    Filtro spam a desarrollar para reconocer si un correo es spam o no.
    Para obtener los datos de aprendizaje se puede utilizar
        datos, clases = carga_datos('mails.data','mails.class')
    Mientras que para obtener los datos de prueba se puede utilizar
        datos, clases = carga_datos('mails_test.data','mails_test.class')
    En la funcion ejemplo_datos viene una manera de mostrar los resultados
    mostrando el valor de las palabras.
    La función debe de devolver el error de predicción tanto con los datos
    de entrenamiento como con los datos de prueba
    """
    error_entrenamiento = 1.0
    error_prueba = 1.0

    #---------------------------------------------------
    # agregar aqui el código
    #---------------------------------------------------
    vocabulario = carga_vocabulario()
    datos, clases = carga_datos('mails.data','mails.class')
    clasificador = nb.NaiveBayes(range(len(datos[0])))
    clasificador.aprende(datos, clases)
    clases_estimadas = clasificador.reconoce(datos)

    """
    Solo para "debuggear" :>
    print clases
    print clases_estimadas  
    """

    error_entrenamiento = naive_bayes.error_clasif(clases, clases_estimadas)
    datos, clases = carga_datos('mails_test.data','mails_test.class')
    clasificador = nb.NaiveBayes(range(len(datos[0])))
    clasificador.aprende(datos, clases)
    clases_estimadas = clasificador.reconoce(datos)
    error_prueba = naive_bayes.error_clasif(clases, clases_estimadas)

    return error_entrenamiento, error_prueba

if __name__ == "__main__":
    ejemplo_datos()
    ee, ep = spam_filter()
    print "El error de entrenamiento es ",ee," %, mientras que el error de predicción es ",ep," %."
