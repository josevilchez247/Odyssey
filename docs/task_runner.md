# Gestor de Tareas

## Introducción
Antes de desplegar una infraestructura virtual, el código tiene que ser testeado,por esta razón el crear los tests y, eventualmente, una forma automática de ejecutarlos 
es un paso previo a llevar a cabo tareas de integración y despliegue continuo.

## Criterios de elección

Para la elección del gestor de tareas hay que tener en cuenta que queremos que tenga el proyecto y donde vamos a desplegarlo. En este caso el proyecto va a ofrecer 
un servicio y para desplegar este servicio voy a utilizar Docker, teniendo esto en cuenta necesito un gestor de tareas que se pueda integrar bien con Docker.
Otro punto a tener en cuenta es el lenguaje del proyecto, en este caso Python, por tanto, necesito un gestor de tareas adecuado para este lenguaje.


## Task Runner

Tras la investigación he podido leer a cerca varios task runner:

1- INVOKE: Invoke es un task runner potente y a la vez cuenta con una sintaxis clara y sencilla, la cual nos permite definir y organizar tareas, entre otras cosas,
desde un único archivo task.py

2- POETHEPOET: Poethepoet es un task runner que trabaja muy bien con Poetry, nos permite definir y organizar las tareas en el mismo fichero pyproject.toml o también
puedes cargar task desde otros archivos. Las tareas se pueden ejecutar en [virtualenv](https://virtualenv.pypa.io/en/latest/)
(es una herramienta para crear entornos Python aislados), lo cuál puede ser de  utilidad a la hora de resolver conflictos de dependencias y versiones.
Las tareas se autodocumentan y pueden tener mensajes opcionales de ayuda. Poethepoet también cuenta con una integración con Docker muy sencilla.

3- HATCH: Hatch es un gestor de proyectos Python moderno y extensible.Al igual que poethepoet nos permite definir las tareas en un mismo archivo pyproject.toml y tambien ejecutar task desde un script. Nos permite crear entornos aislados para pruebas, documentación de creación o cualquier otra cosa que los proyectos necesiten. Incorpora un control de versiones

## Gestor de Dependencias

Tras la elección del task runner (POETHEPOET) hay que elegir un gestor de dependencias, un criterio esencial es que el task runner y el gestor de dependecias trabajen 
bien entre sí, además de ser adecuado para el lenguaje de nuestro proyecto (Python).

Tras la investigación he podido leer a cerca de varios gestores de dependencias para Python:

1- PIP: Pip es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python.Una ventaja importante de pip es la facilidad de su interfaz de línea de comandos, el cual permite instalar paquetes de software de Python fácilmente desde solo una orden. Otra característica particular de pip es que permite gestionar listas de paquetes y sus números de versión correspondientes a través de un archivo de requisitos. Esto nos permite una recreación eficaz de un conjunto de paquetes en un entorno separado o entorno virtual. Esto se puede conseguir con un archivo correctamente formateado requisitos.txt. Con pip es posible instalar un paquete para una versión concreta de Python, sólo es necesario reemplazar ${versión} por la versión de Python que queramos.

2- POETRY: Poetry es una herramienta para la gestión de dependencias y el empaquetado en Python. El archivo pyproject.toml es lo mas importante ya que será el encargado de manejar el proyecto y gestionar las dependencias. Hay que mencionar que podemos definir los test directamente en este mismo archivo al usar poethepoet como task runner, lo cual da mas sencillez al proyecto ya que lo tenemos recogida toda la automatización en un solo fichero.

## Conclusión

Siguiendo los criterios voy a elegir poethepoet como task runner y poetry como gestor de dependencias.

## Bibliografía

[POETHEPOET](https://github.com/nat-n/poethepoet)
[INVOKE](https://www.pyinvoke.org/)
[HATCH](https://github.com/pypa/hatch)
[POETRY](https://python-poetry.org/docs/)
[PIP](https://pypi.org/project/pip/)

