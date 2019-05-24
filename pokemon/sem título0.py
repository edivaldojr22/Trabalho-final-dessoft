import matplotlib.pyplot as plt
from scipy.integrate import odeint
import math
from numpy import arange



def EquacoesDiferenciais(lisSolucoes, t):
    Ya = lisSolucoes[0]
    Xa = lisSolucoes[1]
    Vxa = lisSolucoes[2]
    Vya = lisSolucoes[3]      


    dXadt = Vxa
    dYadt = Vya 
    dVxadt = (-4*math.pi**2)*Xa/(Xa**2 + Ya**2)**(3/2)
    dVyadt = (-4*math.pi**2)*Ya/(Xa**2 + Ya**2)**(3/2)

    


    return[dYadt, dVyadt, dXadt, dVxadt]

#delta t
dt=1e-1
t=arange(0,12,dt)
#condições inciais
Ya0 = 0
Xa0 = 1
Vxa0 = 0
Vya0 = 2*math.pi
Y0=[Ya0, Xa0, Vxa0, Vya0]

S=odeint(EquacoesDiferenciais, Y0, t)

plt.plot(S[:,1], S[:,0])