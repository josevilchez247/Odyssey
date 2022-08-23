﻿# Odyssey
Repositorio del proyecto Odyssey para IV-21/22



## Descripción del proyecto

Quiero crear una aplicación para ahorrar dinero cuando hacemos un viaje.
Esta aplicación va a calcular la mejor ruta desde el origen y el destino pero teniendo en cuenta las características del vehículo dónde viajamos (gasolina/diésel, consumo, capacidad del tanque), 
esta ruta no será la ruta más rápida hasta el objetivo si no que calculará la mejor ruta teniendo en cuenta el precio de la gasolina de las gasolineras más cercanas en el momento que el coche tenga que
repostar.

## Instalación

Para poder usar este proyecto debemos descargar sus ficheros de este repositiorio previamente.

A continuación debemos instalar el gestor de dependencias que vamos a utilizar en este caso Poetry, seguiremmos los pasos de instalación que se indican en la [documentación](https://python-poetry.org/docs/)

```shell
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

Para comprobar si la instalación se ha realizado de forma exitosa podemos hacer

```shell
poetry --version
```

Para resolver las dependencias de nuestro proyecto debemos situarnos en el directorio raiz y hacer la siguiente orden

```shell
poetry install
```

Si queremos agregar algun paquete 
```shell
poetry add requests[security,socks]
```

Para abrir el entorno utilizaremos

```shell
poetry shell
```

Para ver las tareas definidas
```shell
invoke -list
```

Si queremos comprobar la sintaxis del proyecto 
```shell
invoke check
```

## Documentación Adicional 

-> Justificación del gestor de tareas y dependencias [documento]https://github.com/josevilchez247/Odyssey/blob/HidraLerna/docs/gestorTareas.md


