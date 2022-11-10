## Configuración del sistema de integración continua

# Ejecutar tests automáticamente

El principal objetivo de añadir un sistema de integración continua a nuestro proyecto es asegurar que el código pasa todos los tests antes de ser desplegado o simplemente (como en este caso) incorporado a la rama principal, por lo que configuraremos nuestro repositorio para que se pasen los tests automáticamente.

Dado que el sistema de CI elegido es CircleCI, se precisa de un archivo llamado config.yml para su configuración, que se encuentra en la carpeta .circleci. A continuación voy a proceder a explicar su contenido:

- version: 2.1: es la versión de CircleCI incluida por defecto por el generador automático de configuraciones de CircleCI.

Ahora pasamos a definir los jobs necesarios para pasar los tests, en este caso solo será necesario uno, al que llamamos ejecutar-tests:

- executor: éste define la tecnología o entorno subyacente donde se va a ejecutar una tarea. Éstos pueden ser de cuatro tipos: docker, machine, macos o windows. Dado que queremos aprovechar el contenedor de Docker creado en el objetivo anterior (que únicamente contiene los módulos/bibliotecas necesarios para pasar los tests) necesitaremos que nuestro entorno de ejecución (donde se ejecute la tarea) tenga acceso completo al proceso de docker, por esta razón el executor es machine (máquina virtual de linux).
- image: ubuntu-2004:202111-01: en principio la imagen elegida para ejecutar docker no es especialmente relevante en este caso, ya que únicamente ejecutaría el contenedor que ya tenemos para pasar los tests. En este caso se ha elegido la última imagen disponible, que tiene las siguientes especificaciones: Ubuntu 20.04, Docker v20.10.11 y Docker Compose v1.29.2.
- Steps: son los pasos que se van a llevar a cabo en la tarea.
- checkout: comprueba el código fuente del repositorio.
- command: docker run -t -v pwd:/app/test josevilchez247/odyssey: ejecuta los tests sobre el repositorio. El hecho de usar un contenedor para pasar los tests hace que éstos se ejecuten de una forma más rápida y eficiente.

Finalmente, indicamos los jobs que queremos ejecutar, en este caso ejecutar-tests.
CircleCI por defecto pasará los tests automáticamente cada vez que se haga push al repositorio.

# Versiones del lenguaje con las que funciona
En esta configuración se ha decidido testear la aplicación con distintas versiones del lenguaje python. Comprobando las dependencias requeridas por nuestra aplicación,
vemos que las versiones soportadas serían las iguales o superiores a la versión 3.8 de python, por lo que se testeará la aplicación con la versión más antigua soportada por la configuración de poetry, versión 3.8 (última versión estable)
y todas las versiones posteriores, las versiones 3.9 y 3.10. Entre los detalles más importantes de la configuración tenemos:

- strategy: esta palabra clave indica que queremos crear una matriz de compilaciones.
- matrix: será nuestra matriz de compilaciones, esta matriz de compilaciones ejecutará el job varias veces (tres veces en concreto) utilizando distintas versiones de python, que están especificadas en python-version.

Usamos una github action ya definida en el marketplace para establecer la versión de python a usar (3.8, 3.9 y 3.10).
Finalmente, testeamos la aplicación sobre los fuentes del repositorio.
Este job que hemos definido se ejecutará tantas veces como distintas versiones del lenguaje hayamos indicado (en este caso 4) y además, cada uno de estos flujos se ejecutará de forma paralela.


