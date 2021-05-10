import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

gif_name = ''   # Nombre con el que va a exportarse el .gif
pi = np.pi      # Constante pi
c = 1           # Deberia ser 3e8, pero para simular, vamos a usar 1
interval = 200  # Valor de intervalo entre animacion, pueden variarlo para que el gif salga mejor

## TODO - Pedido de valores de entrada (usar l para el largo de la cavidad)

x = np.linspace(0, l, 100)  # Crea una lista que vaya de 0 a l, siendo l
                            # el largo de la cavidad

fig = plt.figure()
ax = plt.axes(xlim=(0, l), ylim=(-2.5, 2.5))
line = [ax.plot([],[])[0] for i in range(3)]    # Crea tres lineas para animar

plt.title('Ondas estacionarias en una cavidad')
ax.set_ylabel('Amplitud')
ax.set_xlabel('Longitud')
ax.grid()

def graph(t):
    """
    Grafica una instancia de la onda viajera, la reflejada y la estacionaria
    """

    # TODO

    # Onda viajera - Senoidal hacia la derecha : usen y_v
    line[0].set_data(x, y_v)

    # Onda reflejada - Senoidal hacia la izquierda : usen y_r
    line[1].set_data(x, y_r)

    # Onda estacionaria : usen y_e
    line[2].set_data(x, y_e)

    return line,

anim = animation.FuncAnimation(fig, graph, 100, interval = interval, repeat = True) # Llama la funcion que grafica periodicamente
anim.save(f'./{gif_name}.gif', writer='PillowWriter', fps=20)                       # Guarda el gif
plt.show()