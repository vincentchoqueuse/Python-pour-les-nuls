from numpy import *             #import de numpy
from pylab import *             #import de matplotlib.pylab
from scipy.stats import norm    #import du module norm de scipy.stats

t=arange(0,5,0.1)
c=[1,2,2]                       #Définition du polynome (t**2+2*t+2)
y=polyval(c,t)                  #Evaluation du polynome
yn=y+norm.rvs(size=len(t))      #Ajout d'un bruit gaussian

c_est = np.polyfit(t, yn, 2)     #regression polynomiale (degré 2)
y_est=polyval(c_est,t)
plot(t,yn,'o',label="mesure")   #Affichage des points
plot(t,y_est,label="regression")#Affichage des points
xlabel('temps')
ylabel('signal')
legend()
show()                          #affichage des courbes