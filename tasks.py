#Fichero para comprobación de la sintaxis y lanzamiento de test

from invoke import task, run

@task
def check(f):
    #Comprobacion de la sintaxis
    
    print("Comprobando errores de sintaxis ... ")
    
    run("pylint --errors-only fuel_station")

@task
def test(f):
    #Comprobación del funcionamiento del código

    print("Realizando test..")


