# Contenedor Docker para la ejecución de test


# Justificación de la Elección

Para llevar a cabo la ejecución de los test que van a probar el código vamos a desplegar un contenedor de docker, dicho contendor debe tener una imagen la cual debe satisfacer las necesidades del proyecto. Como este proyecto es algo académico y solamente se va a utilizar para ejecutar los test,no necesitamos una imagen que pese demasiado y que tenga una gran cantidad de herramientas ya instaladas.

Únicamente lo que nos hace falta es tener python en la imagen, ahora tocaría preguntarse, ¿con qué versión? En un inicio decicí probar la ultima versión python:3.9 y observé que no cumplía con uno de nuestros requisitos básicos, ser ligero, ya que , tenía un tamaño excesivamente grande ~900MB , además del tiempo que se necesitaba para descargar o actualizar la imagen en Dockerhub. Tras esto se probó entre distintas versiones de contenedores base de python como pueden ser alpine y slim. El contenedor base python:3.9-alpine podría ser una buena opción ya que tiene un tamaño muy reducido en comparación con la imagen base del lenguaje ~5 MB, sin embargo, puede tener problemas git y bash por lo que descarté esa opción. El contenedor base python:3.9-slim, al igual que alpine, tiene un tamaño muy reducido, no contiene los paquetes comunes contenidos en la imagen base por defecto y además sólo contiene los páquetes mínimos para poder correr python. Tras crear nuestra imagen usando este contenedor base se pudo comprobar que cumplía nuestros dos requisitos, ser de tamaño reducido y no generar problemas de paquetes no instalados, cosa que ocurría con alpine.

# Github Action

Para actualizar el contenedor docker y subirlo a [DockerHub](https://hub.docker.com/repository/docker/josevilchez4/odyssey) de forma automática he creado un Github Action.
