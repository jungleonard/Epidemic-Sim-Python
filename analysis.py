# Variation du paramètre vaccination_rate
vaccination_rate = [0.001, 0.002, 0.003, 0.005, 0.007 , 0.01 ,0.02 ,0.05]
nb_iter = [70,63,55,51,45,38,27,16]

# Tracer le graphique
plt.plot(vaccination_rate, nb_iter, marker='o', linestyle='-')
plt.title("Nombre d'itérations pour que la maladie disparaisse en fonction de la probabilité de vaccination")
plt.ylabel("Nombre d'itération")
plt.xlabel("Probabilité de vaccination")
plt.show()

# Variation du paramètre initiale_infected
initiale_infected = [10,20,50,75,100,150,200]
nb_iter = [5,5,24,35,38,27,24]

# Tracer le graphique
plt.plot(initiale_infected, nb_iter, marker='o', linestyle='-')
plt.title("Nombre d'itérations pour que la maladie disaparaisse en fonction du nombre d'infecté initialement")
plt.ylabel("Nombre d'itération")
plt.xlabel("nombre d'infecté initialement")
plt.show()
