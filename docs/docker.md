# Contenedor Docker para la ejecución de test


# Justificación de la Elección

Para llevar a cabo la ejecución de los test que van a probar el código vamos a desplegar un contenedor de docker, dicho contendor debe tener una imagen la cual debe satisfacer 
las necesidades del proyecto. Como este proyecto es algo académico y solamente se va a utilizar para ejecutar los test,no necesitamos una imagen que pese demasiado y que tenga una 
gran cantidad de herramientas ya instaladas.

Las opciones que he estudiado han sido [Python](https://hub.docker.com/_/python) y [Alpine](https://hub.docker.com/_/alpine), basándome en lo dicho anteriormente he decido usar
python en concreto la versión slim. Alpine cuenta con una versión slim también con un peso que ronda los ~5 MB,pero he visto que para conseguir que sea tan liguera no incluye
herramientas relacionadas con git y bash por lo que he descartado esta opción, aunque son bastante parecidas, ya que ambas son versiones slim, cuento con que si en algún momento necesito
alguna herramienta tan solo debo añadirlo a las dependencias.
