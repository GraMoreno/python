#Programa para calcular la altura de una pelota en movimiento vertical
# -*- coding: utf-8 -*-
v0= 5    #velocidad inicial
g= 9.81  #aceleracion de la gravedad
t=0.6    #tiempo
y= v0*t - 0.5*g*t**2  #posicion vertical
print ("""En el tiempo t={t:f} s, la pelota 
con velocidad inicial v0={v0:.3E} m/s
se encuentra ubicada en la altura {y:.2f} m.
""" .format(t=t, v0=v0, y=y))