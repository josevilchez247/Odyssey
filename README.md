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

Una vez instalado, podremos añadir dependencias de manera muy simple.

```shell
invoke installdeps
```

con esto lo añadiremos a las dependencias de desarrollo de nuestro repositorio.
Por último nos queda instalar todas las dependencias

```shell
invoke installdeps
```
de esta forma, todas las dependencias que aparecen en el archivo pyproject.toml se instalarán.
Para comprobar que el código compila usaremos el comando

```shell
invoke check
```

Para los test usaremos el comando

```shell
invoke test


## Principios F.I.R.S.T
En los tests desarrollados, he seguido los pasos F.I.R.S.T.
- **Fast** -> Porque los test son rápidos.
- **Independent** -> No dependen los unos de los otros.
- **Repeatable** -> El resultado de los test son los mismos independientemente de donde se ejecuten.
- **Self-validating** -> Se podrian ejecutar de manera automatica. 

## Documentación Adicional 

- Documentación adicional [aquí](https://github.com/josevilchez247/Odyssey/blob/ToroCreta-4/docs/historias-usuario.md)

- Justificación del gestor de tareas y dependencias [documento](https://github.com/josevilchez247/Odyssey/blob/HidraLerna-3/docs/task_runner.md)

- Justificación del test runner y la biblioteca de aserciones [documento](https://github.com/josevilchez247/Odyssey/blob/ToroCreta-4/docs/test.md)

- Justificación imagen del contenedor de docker [documento](https://github.com/josevilchez247/Odyssey/blob/CiervaCerinea-5/docs/docker.md)
