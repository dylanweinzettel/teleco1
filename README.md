# Especificaciones

Van a encontrar una serie de problemas en el repositorio para resolver con `LaTeX`. Cuando lo hagan, van a escribir un `README.md` con este contenido:

```markdown
# Electromagnetismo

Alumno: Apellido y nombre
Curso: Curso
Materia: Telecomunicaciones I

## Resoluciones

### Problema 1

[Ecuaciones que hayan usado]
...

```

## Problemas para resolver

### Problema 1

Un láser de dióxido de carbono emite una onda electromagnética senoidal que viaja en el vacío en la dirección +x. La longitud de onda es 10.6 µm y el campo eléctrico es paralelo al eje z, con magnitud máxima de 1.5 MV/m. Halle la magnitud máxima del campo magnético y escriba las ecuaciones vectoriales de ambos campos. Recuerde que 1 V = 1 Wb/s y 1 Wb/m^2 = T (Tesla, unidad de campo magnético).

### Problema 2

Una onda electromagnética sinusoidal se propaga en el vacío en la dirección +z. El campo eléctrico tiene una oscilación máxima de 4 V/m en la dirección +y. ¿Cuál es la dirección y magnitud del campo magnético en el instante que la oscilación del campo eléctrico es máxima?

### Problema 3

Suponga que un día sale de una joyería con un diamante y lo sostiene contra la luz de una lámpara de calle. La luz amarilla que emite la lámpara tiene una frecuencia de 5.09 x 10^14 Hz. Determine la longitud de onda en el vacío, la velocidad de propagación de la onda y la longitud de onda en el diamante, sabiendo que la permitividad relativa es 5.84 y la permeabilidad relativa es 1.00.

### Problema 4

Una onda de radio con frecuencia de 90 MHz (banda FM de la radio) pasa del vacío a un núcleo de ferrita aislante (material ferromagnético que se usa en los cables de computadora para eliminar las interferencias de radio). Determine la longitud de onda en el vacío, así como la velocidad de propagación y la longitud de onda en la ferrita, sabiendo que la permitividad y permeabilidad relativa son 10 y 1000 respectivamente a esa frecuencia.

## Como entregar

Pongan el `README.md` en alguna carpeta nueva y luego corran en una terminal:

```
git init
git add README.md
git commit -m "Initial commit"
git checkout -b teleco1/2021/em/electromagnetismo
git push https://github.com/trq20/USERNAME.git teleco1/2021/em/electromagnetismo
```

Donde USERNAME es su nombre de usuario. Pueden verificar que se haya subido visitando `https://github.com/trq20/USERNAME/tree/teleco1/2021/em/electromagnetismo`.

