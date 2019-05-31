# -*- coding: utf-8 -*-
"""
Created on Wed May 29 00:05:27 2019

@author: jpfa1
"""

import matplotlib.pyplot as plt
from scipy.integrate import odeint
import math
from numpy import arange


def eq(S, tempo):
    X= S[0]
    Y= S[2]
    Vx= S[1]
    Vy= S[3]      
    T = math.atan(X/Y)
    
    DyDt = Vy
    DvyDt = (k((Y*math.cos(T))-l0)* math.sin((math.pi/2) - T))/m - (p*Vy**2*Cd*a*math.cos((math.pi/2) - T))/2*m -g
    DxDt = Vx
    DvxDt = g + (p*Vx**2*Cd*a*math.cos((math.pi/2) - T))/2*m  -(k((Y*math.cos(T))-l0)* math.sin((math.pi/2) - T))/m
    return [DxDt, DvxDt, DyDt, DvyDt]
    


l0 = 30
r = 10
m = 220
g = 10
Cd = 1.5
p = 1
k = 10
a = math.pi*r**2


dt=1e-2
tempo = arange(0,20,dt)


X0 = 55
DvxDt0 = 0
Y0 = 0
DvyDt0 = 0
IN = [X0, DvxDt0, Y0, DvyDt0]

S = odeint(eq, IN, tempo)

plt.plot(S[0], S[2])
plt.show()