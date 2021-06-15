import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

def graficar(tita, na, nb):

    plt.xlim([-10, 10])                     # Limite en x: total 20 unidades
    plt.ylim([-10, 10])                     # Limite en y: total 20 unidades
    plt.hlines(0, -10, 10, colors='black')  # Superficie de contacto
    plt.vlines(0, -10, 10, colors='black', linestyles='dashed') # Normal a la superficie
    plt.title("Reflexion/Refraccion")
    plt.grid()
    
    tita_crit = np.rad2deg(np.arcsin( nb / na ))    # Calculo el angulo para el que no se puede
                                                    # refractar
    if nb < na and tita > tita_crit:

        plt.plot(0, 0, label='Error de refraccion')

    else:

        pass
        # TODO
    
    plt.legend()
    plt.show()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        sliders = [
            {"name" : "tita", "from" : 0, "to" : 90, "label" : "Angulo de incidencia (\u03B8)", "res" : .5},
            {"name" : "na", "from" : 1, "to" : 1.5, "label" : "Indice de refraccion 1 (na)", "res" : .01},
            {"name" : "nb", "from" : 1, "to" : 1.5, "label" : "Indice de refraccion 2 (nb)", "res" : .01}
        ]

        for s in sliders:

            slider = tk.Scale(self, from_ = s["from"], to_=s["to"], label=s["label"], resolution=s["res"], orient="horizontal", sliderlength="10px", length="120px")
            setattr(self, s["name"], slider)
            getattr(self, s["name"]).pack()

        self.draw = tk.Button(self, text="Graficar", command=lambda: graficar(self.tita.get(), self.na.get(), self.nb.get()))
        self.draw.pack()
        self.quit = tk.Button(self, text="Salir", command=self.master.destroy)
        self.quit.pack(side="bottom")

root = tk.Tk()
app = Application(master=root)
app.mainloop()

