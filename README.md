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

## Principios F.I.R.S.T
En los tests desarrollados, he seguido los pasos F.I.R.S.T.
- **Fast** -> Porque los test son rápidos.
- **Independent** -> No dependen los unos de los otros.
- **Repeatable** -> El resultado de los test son los mismos independientemente de donde se ejecuten.
- **Self-validating** -> Se podrian ejecutar de manera automatica. 

## Integración Continua

Nuestros sistemas de integración continua deben de cumplir con una serie de requisitos para su aceptación:

- Que sean sencillos de configurar, tanto para pasar los tests automáticamente como para probar con distintas versiones del lenguaje la aplicación.
- Que el checks API pueda ser configurado fácilmente.

Hoy en día existe una gran variedad de sistemas de integración continua que pueden usarse para nuestros proyectos, entre los que se pueden encontrar los siguientes:

- Github Actions
- Travis
- Circle CI
- Semaphore CI
- AppVeyor
- Jenkins

Teniendo en cuenta ésto, vamos a realizar una búsqueda de los sistemas de integración continua que cumplen los requisitos especificados más arriba. Comenzaremos eligiendo el necesario para pasar los tests automáticamente y posteriormente el segundo sistema de CI, necesario para testear la aplicación con distintas versioens del lenguaje.

Atendiendo a la facilidad de uso y lo estándar que es el sistema, Travis es probablemente el más recomendado de usar, ya que permite ver el resultado de la integración continua en la misma página de Github (checks API) de manera muy sencilla. Sin embargo, dado que para darse de alta exigen tarjeta de crédito (lo cual no todo el mundo posee), se ha descartado como opción. Dado que en el objetivo anterior se usó Github Actions para configurar la actualización del docker, he decidido descartar usarlos ya que en los tests de la asignatura se comprobará que se haya configurado un sistema de integración continua distinto a Github Actions. Siguiendo con la comparativa de los sistemas de CI disponibles, si tuviéramos que elegir entre Circle CI y Semaphore CI, Circle CI es más aceptado por la comunidad. Además de ésto se ha comprobado cuál de los dos es el más utilizado actualmente mediante distintos rankings como este o este, en el que CircleCI se encuentra en la 3ª posición y SemaphoreCI en la 16ª y en el que CircleCI está en la 5ª posición y SemaphoreCI en la 10ª, respectivamente. Con respecto al resto de sistemas de CI (AppVeyor y Jenkins), decir que Jenkins es el más popular actualmente, sin embargo, no es sólo un sistema de integración continua sino que además es un sistema de entrega/implementación continua, por lo que se ha descartado como opción.

Tras esta comparación, he decidido usar como primer sistema de integración continua CircleCI ya que es sencillo de usar, fácilmente configurable, permitiendo incluir fácilmente el checks API, de forma que se puedan ver los resultados de la integración continua en Github. Además, nos permite crear y editar el archivo de configuración de la integración continua, llamado config.yml desde su interfaz web, corrigiendo errores sintácticos y permitiendo hacer commits del archivo directamente a la rama en la que nos encontremos.

Otro de los puntos a cubrir de la integración continua es comprobar con qué versiones del lenguaje funciona nuestra aplicación. Para ello, he decidido usar como segundo sistema de CI las Github Actions de Github, entre otras cosas porque al buscar un poco de información sobre el uso de la matrix he podido comprobar que la configuración es muy sencilla. Además, es obvia la gran integración que tienen con Github, no necesitando ningún tipo de configuración previa para poder ver el resultado de los workflows.

## Documentación Adicional 

- Documentación adicional [aquí](https://github.com/josevilchez247/Odyssey/blob/ToroCreta-4/docs/historias-usuario.md)

- Justificación del gestor de tareas y dependencias [documento](https://github.com/josevilchez247/Odyssey/blob/HidraLerna-3/docs/task_runner.md)

- Justificación del test runner y la biblioteca de aserciones [documento](https://github.com/josevilchez247/Odyssey/blob/ToroCreta-4/docs/test.md)

- Justificación imagen del contenedor de docker [documento](https://github.com/josevilchez247/Odyssey/blob/CiervaCerinea-5/docs/docker.md)
