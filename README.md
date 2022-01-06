# Odyssey
Repositorio del proyecto Odyssey para IV-21/22



## Descripción del proyecto

Quiero crear una aplicación para ahorrar dinero cuando hacemos un viaje.
Esta aplicación va a calcular la mejor ruta desde el origen y el destino pero teniendo en cuenta las características del vehículo dónde viajamos (gasolina/diésel, consumo, capacidad del tanque), 
esta ruta no será la ruta más rápida hasta el objetivo si no que calculará la mejor ruta teniendo en cuenta el precio de la gasolina de las gasolineras más cercanas en el momento que el coche tenga que
repostar.

##Instalación

Para poder usar este proyecto debemos descargar sus ficheros de este repositiorio previamente.

A continuación debemos abrir una terminal y hacer una instalación de Invoke

```shell
pip install invoke
```

Una vez tenemos invoke instalado lo usaremos para instalar las dependencias de nuestro proyecto para lo que usaremos en la terminal la siguiente orden

```shell
invoke installdeps
```

Con esto ya tendriamos instaladas las depencias de nuestro proyecto si queremos hacer una comprobación de la sintaxis para ver si es correcta debemos utilizar la siguiente orden

```shell
invoke check
```

Para lanzar los test de comprobación del programa tenemos la siguiente orden

```shell
invoke test
```


