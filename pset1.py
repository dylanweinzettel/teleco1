import matplotlib.pyplot as plt     # Modulo para graficar
import numpy as np                  # Modulo con algunos metodos matematicos utiles

# Lista de frecuencias para graficar (100MHz, 300MHz, 500MHz, 1GHz, 3GHz)
frecuencias = [100e6, 300e6, 500e6, 1e9, 3e9]   

c = 3e8     # Velocidad de la luz
pi = np.pi  # Numero pi

# Lista de valores para evaluar cada onda entre 0 y 1 ns. Tiene 1000 puntos para evaluar
time = np.linspace(0, 1e-9, 1000)

# Este es un ejemplo de como usar plt.plot. Pueden quitar el comentario para probarlo
# plt.plot([0,1,2,3,4],[0,1,4,9,16],label='esta es una etiqueta')

# Para calcular un punto una onda senoidal, usen np.sin()

for freq in frecuencias:

    plt.plot(time, np.sin(2*pi*freq*time), label='F={:.1e} Hz | \u03BB={:.0e} m'.format(freq, c/freq))


plt.title('Ondas')      # Titulo del grafico
plt.xlabel('t [s]')     # Etiqueta para el eje X
plt.ylabel('Amplitud')  # Etiqueta para el eje Y

plt.grid()      # Muestra una grilla en el grafico
plt.legend()    # Muestra los labels que asignen a cada onda
plt.show()      # Muestra todas las figuras que hayan graficado