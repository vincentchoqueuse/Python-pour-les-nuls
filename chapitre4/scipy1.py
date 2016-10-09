from numpy import *             #import de numpy
from scipy import signal        #import du module signal de scipy
from pylab import *             #import de matplotlib.pylab

Fe=100                          #fréquence d'échantillonnage
t = arange(0, 0.5, 1/Fe)        #creation de la base temps avec numpy
s = sin(2*pi*10*t)              #creation d'une sinusoide à 10hz
f,Pxx=signal.periodogram(s,Fe)  #calcul du periodogram
f2,Px2=signal.periodogram(s,Fe,None,10*Fe)  #calcul du periodogram avec zero padding

plot(f,Pxx,label="periodogramme")   #Affichage via la fonction plot de Matplotlib
plot(f2,Px2,label="periodogramme avec zero padding")
xlabel('Frequence (Hz)')        #définition de l'axe des abscisses
ylabel('Module')                #définition de l'axe des ordonnées
legend()
show()                          #affichage des courbes