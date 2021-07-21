import matplotlib.pyplot as plt
import numpy as np
from random import choice

lambdas = [i for i in range(1, 5)]

l = choice(lambdas)     # Elige una longitud de onda entre las posibles

lim = 20
vals = np.arange(-lim, lim + .25, .25)  # Arma una lista de puntos para analizar

plt.plot([-10, 10], [0, 0], 'ro', color='green', label=f'\u03BB = {l}') # Plotea los puntos de origen de las ondas
plt.xlim(-lim, lim)
plt.ylim(-lim, lim)
plt.grid()

# TODO

plt.legend()
plt.show()
