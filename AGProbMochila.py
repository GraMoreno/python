# -*- coding utf-8 -*-
""" Creado al día 21/5/2020 
"""
import datetime
import random
random.seed(2)
tiempoInicio= datetime.datetime.now()

conjGene = 'abcdefghigklmnopkrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
objetivo ='HolaMundo'

def crear_padres(longitud):
    genes = []
    while len(genes) < longitud:
        tamanoEj = min(longitud - len(genes), len(conjGene))
        genes.extend(random.sample(conjGene, tamanoEj))
    return ''.join(genes)

def funcion_aptitud(adivina):
    return sum(1 for esperado, actual in zip(objetivo,adivina) if esperado == actual)

def mutacion(padres):
    indice = random.randrange(0,len(padres))
    genesHijo= list(padres)
    nuevoGene, alternar = random.sample(conjGene,2)
    genesHijo[indice] = alternar if nuevoGene == genesHijo[indice] else nuevoGene
    return ''.join(genesHijo)

def mostrar(adivina):
    difTiempo = datetime.datetime.now() - tiempoInicio
    fitness = funcion_aptitud(adivina)
    print('{}\t{}\t{}'.format(adivina, fitness,difTiempo))

mejorPadre = crear_padres(len(objetivo))
mejorFitness= funcion_aptitud(mejorPadre)
mostrar(mejorPadre)

while True:
    hijo = mutacion(mejorPadre)
    hijoFitness = funcion_aptitud(hijo)
    if mejorFitness >= hijoFitness:
        continue
    mostrar(hijo)
    if hijoFitness >= len(mejorPadre):
        break
    mejorFitness= hijoFitness
    mejorPadre = hijo
