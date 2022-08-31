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

## Conclusión

Siguiendo los criterios voy a elegir poethepoet como task runner.
