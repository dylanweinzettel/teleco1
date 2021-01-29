# Ondas

### Formula

$$
\lambda = \frac{C}{f} \space con \space C = 3 \times 10^{8} \frac{m}{s}
$$

**Nota**: La fórmula usa la velocidad de propagación en vez de la velocidad de la luz (C), pero como en la mayoría de los casos trabajamos con ondas electromagnéticas que se propagan en el espacio libre, usamos C, si eso no es así, se va a aclarar. 

## Resolver

---

### La longitud de onda de una onda con:
- 1 s de período.
- 3 GHz de frecuencia.

### La frecuencia de una onda con:
- 3 mm de longitud de onda.
- 15 us de período.

### El período de una onda con:
- 9 Km de longitud de onda.
- 10 KHz de frecuencia.

## Graficar

---

Con este `README` van a encontrar un `pset1.py`. Dentro, van a encontrar una lista de frecuencias para las que tienen que graficar la onda correspondiente e indicar su longitud de onda. Tiene que quedar algo parecido a esto:

![](./graph.png)

### Ayudas
- El método `plt.plot()` sirve para graficar una serie de puntos. Hay un ejemplo en el programa.
- Pueden encontrar ayuda para darle formato al string que usen como label para el gráfico en esta [página](https://www.w3schools.com/python/ref_string_format.asp).
- Recuerden que una onda se describe como:
$$
f_{(t)}=A sin(2\pi f t)
$$
Donde: A es la amplitud (pueden usar 1), f es la frecuencia y t es el tiempo en el que se calcula la onda.
- Van a necesitar algún tipo de bucle para recorrer la lista que tiene los valores de t donde van a analizar la onda. Hay muchas formas de hacerlos en Python, algunas mas eficientes que otras. Pueden ver algunos ejemplos en esta [página](https://www.w3schools.com/python/python_for_loops.asp).