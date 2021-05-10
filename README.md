# Especificaciones

Escribir un programa que:

- Tome como entrada una longitud (en `cm`) que corresponde al largo de la cavidad.
- Tome como entrada una cantidad de armónicos que va a graficar.
- Grafique las ondas viajera, reflejada y estacionaria que entrarían en esa cavidad, con la onda estacionaria teniendo la cantidad de armónicos establecido.

Por ejemplo, para las siguientes entrada:

```
Inserte el largo de la cavidad (cm): 12
Inserte la cantidad de armonicos: 3
```

La salida debería ser:

![cavidad.gif](./cavidad.gif)

Hacer tres pruebas distintas y guardar los `.gif` de cada una e identificar la distancia del cero a la que se produce cada `nodo`. Por ejemplo, en el de arriba los nodos ocurren en:

- Nodo 1: 0 cm
- Nodo 2: 4 cm
- Nodo 3: 8 cm
- Nodo 4: 12 cm

Luego, armar un `README.md` con lo siguiente:

```markdown
# Ondas Estacionarias

Alumno: Apellido y nombre
Curso: Curso
Materia: Telecomunicaciones I

## Primera prueba

[Insertar .gif]
[Identificar nodos]

## Segunda prueba

[Insertar .gif]
[Identificar nodos]

## Tercera prueba

[Insertar .gif]
[Identificar nodos]
```

## Consideraciones

- Pueden cambiar la variable `gif_name` para que cada vez que corran el programa, el `.gif` se guarde con otro nombre.
- La variable `interval` en `ms` la pueden variar para que la animación sea mas fluida o lenta.
- Para guardar la longitud de la cavidad, declaren una variable `l`. Muchas cosas en el programa dependen de eso.

## Como entregar

Pongan el `README.md`, `cavidad.py` y los `.gif` en una carpeta aparte y corran en la terminal:

```
git init
git add .
git commit -m "Initial commit"
git checkout -b teleco1/2021/em/estacionarias
git push https://github.com/trq20/USERNAME.git teleco1/2021/em/estacionarias
```

Donde `USERNAME` es su nombre de usuario. Pueden verificar que se haya subido visitando `https://github.com/trq20/USERNAME/tree/teleco1/2021/em/estacionarias`.