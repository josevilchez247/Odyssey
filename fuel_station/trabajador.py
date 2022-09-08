#
# ────────────────────────────────────────────────────────────────────
#   :::::: trabajador.py : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────────────
#

# ─── PROYECT: Odyssey (https://github.com/josevilchez247/Odyssey) ───────────────
# ─── MODULE: fuel_station ───────────────────────────────────────────────────────
# ─── OWNER: @josevilchez247 ─────────────────────────────────────────────────────
# ─── AUTHOR: @josevilchez247 ────────────────────────────────────────────────────────
# ─── DATE: 8-09-2022 ────────────────────────────────────────────────────────────
# ─── VERSION: 1.8 ───────────────────────────────────────────────────────────────

from enum import Enum


# Enumerador que define los distintos tipos de gasolina
class FuelType(Enum):
    DIESEL = "diesel"
    DIESEL_PLUS = "diesel_plus"
    GASOLINA = "gasolina"

class Trabajador:
  
   def __init__(self, ID, id_fuel_station, name, clave):
        self.ID = ID                            # Identificador único
        self.id_fuel_station = id_fuel_station  # Identificador de la gasolinera donde esta dado de alta el trabajador
        self.name = name                        # Nombre del trabajador
        self.clave = clave                      # Clave de acceso del trabajador
        
        
    # Método que actualiza el precio para un tipo de gasolina en la BD 
    def set_fuel_price(self, fuel_type, price):
        #Enviar el precio a la BD 
  
