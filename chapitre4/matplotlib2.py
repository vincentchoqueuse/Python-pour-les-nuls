from numpy import *             #import de numpy
from pylab import *             #import de matplotlib.pylab

t = arange(0, 1, 1/1000)        #creation de la base temps avec numpy
s = sin(2*pi*10*t)              #creation d'une sinusoide à 10hz
s2 = cos(2*pi*10*t)              #creation d'une sinusoide à 10hz

plot(t, s,label="sinus")        #Affichage via la fonction plot de Matplotlib
plot(t, s2,label="cosinus")
xlabel('Temps (s)')             #définition de l'axe des abscisses
ylabel('Amplitude')             #définition de l'axe des ordonnées
legend()                        #ajout de la légende
show()                          #affichage des courbes