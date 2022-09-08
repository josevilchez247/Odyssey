#
# ────────────────────────────────────────────────────────────────────
#   :::::: fuel_station.py : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────────────
#

# ─── PROYECT: Odyssey (https://github.com/josevilchez247/Odyssey) ───────────────
# ─── MODULE: fuel_station ───────────────────────────────────────────────────────
# ─── OWNER: @josevilchez247 ─────────────────────────────────────────────────────
# ─── AUTHOR: @jantoniovr ────────────────────────────────────────────────────────
# ─── DATE: 8-10-2021 ────────────────────────────────────────────────────────────
# ─── VERSION: 1.0 ───────────────────────────────────────────────────────────────

from enum import Enum


# Enumerador que define los distintos tipos de gasolina
class FuelType(Enum):
    DIESEL = "diesel"
    DIESEL_PLUS = "diesel_plus"
    GASOLINA = "gasolina"

# ────────────────────────────────────────────────────────────────────────────────

# Clase que modela una gasolinera
class FuelStation:

    def __init__(self, ID, name, location, empleados, fuel_prices):
        self.ID = ID                    # Identificador único
        self.name = name                # Nombre de la gasolinera
        self.location = location        # Localización de la gasolinera
        self.empleados = empleados      # Empleados que trabajan en esa gasolinera

        # Diccionario cuya clave es el tipo de gasolina y el valor es el precio oficial de la gasolina y el sugerido por los clientes en los comentarios
        # El argumento fuel_prices es un diccionario que almacena los precios 
        self.fuel_prices = {
            FuelType.DIESEL: [fuel_prices[FuelType.DIESEL],0],
            FuelType.DIESEL_PLUS: [fuel_prices[FuelType.DIESEL_PLUS],0],
            FuelType.GASOLINA: [fuel_prices[FuelType.GASOLINA],0]
        }

    # Método que cambia un precio oficial para un tipo de gasolina
    def set_fuel_price(self, fuel_type, price):
        self.fuel_prices[fuel_type][0] = price
        
    # Método que cambia un precio sugerido para un tipo de gasolina
    def set_fuel_price_suggested(self, fuel_type, price):
        self.fuel_prices[fuel_type][1] = price

    # Método de clase que busca en la BD la gasolinera dado su identificador
    # y construye y devuelve un objeto de la clase FuelStation con los datos
    # obtenidos
    @classmethod
    def look_for_fuel_station_by_ID(cls, ID):
        # Buscar en la BD y construir el objeto fuel_station cuyo id es ID
        pass

# ────────────────────────────────────────────────────────────────────────────────
