# Biblioteca de aserciones y test runner

## Biblioteca de aserciones

Criterios que ha de cumplir nuestra biblioteca para nuestro proyecto:

1- Estado de desarrollo maduro.

2- Un buen soporte, ya que queremos, poder resolver cualquier duda de manera rápida, es decir que tenga una comunidad activa, debido a la característica
de nuestro proyecto, se está realizando para una asignatura y posteriormente no se continuará con su desarrollo.

3- Assert que me ayuden a la hora de desarrollar el código.

4- Sencillez de uso y sintaxis.

Teniendo en cuenta estos criterios investigué a cerca de Grappa, Asserpy y Verify:

[Grappa](https://pypi.org/project/grappa/) me encontré con que el estado de desarrollo es estable, pero aún no está maduro, por lo que quizás pueda encontrarme
con problemas a corto plazo y además de eso las assert con las que cuenta no terminaron de convencerme.

[Verify](https://pypi.org/project/verify/) con verify el estado de desarrollo aún no es ni estable, además cuenta con pocos PR y proyectos por lo que puede ser difícil
encontrar soluciones ante problemas que me puedan surgir.

[Asserpy](https://github.com/assertpy/assertpy) Asserpy es una biblioteca de aserciones simples para pruebas unitarias en Python con una API fluida y agradable.
Soporta Python 2 y 3. Es muy fácil de usar, simplemente importamos la función y ya podemos usarla, funciona aún mejor con test runner como Pytest o Nose.

Teniendo todo esto en cuenta he decido utilizar Asserpy.

## Test runner

Tras la investigación y elección de la biblioteca de aserciones vi las mejores opciones para complementarla eran [pytest](https://pypi.org/project/pytest/) o [Nose](https://nose.readthedocs.io/en/latest/).
Pero al investigar ambas opciones vi que pytest es mejor opción, ya que Nose se encuentra actualmente sin mantenimiento, ya que se está desarrollando [Nose2](https://github.com/nose-devs/nose2)
y en cuya documentación podemos ver que actualmente recomiendan usar pytest, ya que este marco de pruebas cuenta con un gran mantenimiento y una gran comunidad, además pytest cumple todos los requisitos que estamos buscando.
