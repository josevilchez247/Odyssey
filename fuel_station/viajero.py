#
# ────────────────────────────────────────────────────────────────────
#   :::::: viajero.py : :  :   :    :     :        :          :
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

class Viajero:
  
   def __init__(self, ID, name, clave):
        self.ID = ID                            # Identificador único
        self.name = name                        # Nombre del viajero
        
    # Método para obtener el id de la gasolinera que nos encontramos
    def get_id_fuel_station(self,localizacion):
        #Consultamos a la base de datos el id por l alocalización
        id_fuel_station = getIDFuelStationBD(localizacion)
        self.set_fuel_price(self,id_fuel_station,fuel_type,price)
        
        
    # Método que actualiza el precio para un tipo de gasolina en la BD 
    def set_fuel_price(self,id_fuel_station ,fuel_type, price):
        #Enviar el precio a la BD 
