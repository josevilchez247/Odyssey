#Fichero para la instalación de dependencias, lanzamiento de test y comprobacio  de la sintaxis.

from invoke import task, run

@task
def installdeps(f):
    #Instalacion de las dependencias del programa
    
    print("Instalando...")
    run("pip install -r requirements.txt")

@task
def test(f):
    #Comprobación del funcionamiento del código

    print("Realizando test..")

@task
def check(f):
    #Comprobacion de la sintaxis
    
    print("Comprobando errores de sintaxis ... ")
    
    run("pylint --errors-only fuel_station")
