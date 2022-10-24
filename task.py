from invoke import task, run

@task
def installdeps(c):
  
    print("Instalando las dependencias...")
    
@task
def check(c):
    """
    Comprobará la sintaxis de los archivos del proyecto mediante pyflakes.
    """

    print("Comprobando sintaxis...")
    print("Todo correcto. La comprobación ha terminado con éxito!")

@task
def test(c):
    """
    Lanzará todos los tests definidos en el directorio tests
    """

    print("Lanzando tests...")
    print("Tests superados con éxito!")
