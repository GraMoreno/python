#Programa para calcular la altura de una pelota en movimiento vertical
# -*- coding: utf-8 -*-
import math
#from math import sqrt
#from math import sqrt, exp, log, sin
#from math import *
v0= 5    #velocidad inicial
g= 9.81  #aceleracion de la gravedad
yc=0.2    #
t1=(v0 - math.sqrt(v0**2 - 2*g*yc))/g
t2=(v0 + math.sqrt(v0**2 - 2*g*yc))/g
print ("el tiempo  t=%g s y %g s,  la altura es %g  m." %(t1,t2,yc))
