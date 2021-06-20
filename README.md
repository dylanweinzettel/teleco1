## Especificaciones

Escribir un programa que:

- A partir de un ángulo de incidencia (`ϴa`) y los índices de refracción de dos materiales (`na` y `nb`), grafique un haz incidente, su reflejado y refractado correspondiente.
- Muestre el valor de los ángulos incidente y refractado (`ϴa` y `ϴb`) como label de cada haz. Los valores deben estar en grados.
- Hacer dos pruebas, una para `na > nb` y otra para `nb > na` y guardar los gráficos resultantes.

Luego, hacer un `README.md` con lo siguiente:

```markdown
# Reflexión y refracción

Alumno: Nombre y apellido
Curso: Curso
Materia: Telecomunicaciones I

## Ejemplo na > nb
[imagen obtenida]

Datos:
- `ϴa`
- `na`
- `nb

## Ejemplo nb > na
[imagen obtenida]

Datos:
- `ϴa`
- `na`
- `nb
```

## Consideraciones

- Recuerden que los ángulos los medimos siempre respecto a la normal de la superficie (la linea punteada que van a ver en el gráfico).
- Bajo ciertas condiciones, puede que obtengan un mensaje en el gráfico de `Error de refracción`. Es normal, va a ser algo para explicar luego.
- Para graficar las tres rectas, es probable que tengan que usar algo de trigonometría. Pueden importar las funciones trigonométricas con:

```python
from numpy import sin, cos, tan
```

- Tengan en cuenta que las funciones trigonométricas trabajan en `radianes` no en `grados`.
- La ley que rige la refracción es la `Ley de Snell` y se expresa como:

<div align=center>
  <img src="https://render.githubusercontent.com/render/math?math=n_a sin(\theta_a) = n_b sin(\theta_b)">
</div>

## Ejemplo

El resultado debe ser parecido a esto:

![ejemplo](./ejemplo,PNG)

Los datos son:
- `na` = 1.15
- `nb` = 1.05

## Como entregar

Pongan el `README.md`, la imagen y el `refraccion.py` en una carpetan, abran una terminal y escriban:

```
git init
git add README.md refraccion.py img.PNG
git commit -m "Initial commit"
git checkout -b teleco1/2021/optica/refraccion
git push https://github.com/trq20/USERNAME.git teleco1/2021/optica/refraccion
```

Donde USERNAME es su nombre de usuario. Pueden verificar que se haya subido visitando `https://github.com/trq20/USERNAME/tree/teleco1/2021/optica/refraccion`.
