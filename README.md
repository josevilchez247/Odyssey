# Odyssey
Repositorio del proyecto Odyssey para IV-21/22



## Descripción del proyecto

Quiero crear una aplicación para ahorrar dinero cuando hacemos un viaje.
Esta aplicación va a calcular la mejor ruta desde el origen y el destino pero teniendo en cuenta las características del vehículo dónde viajamos (gasolina/diésel, consumo, capacidad del tanque), 
esta ruta no será la ruta más rápida hasta el objetivo si no que calculará la mejor ruta teniendo en cuenta el precio de la gasolina de las gasolineras más cercanas en el momento que el coche tenga que
repostar.

## Instalación

Para poder usar este proyecto debemos descargar sus ficheros de este repositorio previamente.

Para comprobar si la instalación se ha realizado de forma exitosa podemos hacer

```shell
poetry --version
```

Una vez instalado, podremos añadir dependencias de manera muy simple. En nuestro caso necesitamos añadir Poethepoet y lo agregaremos de esta forma:

```shell
poetry self add 'poethepoet[poetry_plugin]'
```

con esto lo añadiremos a las dependencias de desarrollo de nuestro repositorio.
Por último nos queda instalar todas las dependencias

```shell
poetry poe installdeps
```
de esta forma, todas las dependencias que aparecen en el archivo pyproject.toml se instalarán.
Para comprobar que el código compila usaremos el comando

```shell
poetry poe check
```

Para los test usaremos el comando

```shell
poetry poe test
```

## Documentación Adicional 

-> Justificación del gestor de tareas y dependencias [documento](https://github.com/josevilchez247/Odyssey/blob/HidraLerna-3/docs/task_runner.md)
-> Justificación del test runner y la biblioteca de aserciones [documento](https://github.com/josevilchez247/Odyssey/blob/ToroCreta-4/docs/test.md)


