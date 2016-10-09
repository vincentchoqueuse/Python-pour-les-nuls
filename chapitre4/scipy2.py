from numpy import *             #import de numpy
from pylab import *             #import de matplotlib.pylab
from scipy.stats import norm    #import du module norm de scipy.stats

r=norm.rvs(size=1000)           #Réalisation aléatoire suivant une loi gaussienne
moyenne=mean(r)                 #calcul de la moyenne
variance=var(r)                 #calcul de la variance
print("Moyenne: %f, variance: %f" %(moyenne,variance))

plot(r)                         #Affichage de la réalisation aléatoire via la fonction plot de Matplotlib
xlabel('Echantillons')
ylabel('Valeur')

figure()                        #création d'une nouvelle figure
hist(r, histtype='stepfilled')  #affichage de l'histogramme
xlabel('Valeur')
ylabel('Nb occurences')

show()                          #affichage des courbes