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

    def __init__(self, ID, name, location, fuel_prices):
        self.ID = ID                    # Identificador único
        self.name = name                # Nombre de la gasolinera
        self.location = location        # Localización de la gasolinera

        # Diccionario cuya clave es el tipo de gasolina y el valor es el precio de la gasolina
        # El argumento fuel_prices es un diccionario que almacena los precios
        self.fuel_prices = {
            FuelType.DIESEL: fuel_prices[FuelType.DIESEL],
            FuelType.DIESEL_PLUS: fuel_prices[FuelType.DIESEL_PLUS],
            FuelType.GASOLINA: fuel_prices[FuelType.GASOLINA]
        }

        # Diccionario cuya clave es el tipo de gasolina y el valor es True si está verificado
        # o False en caso de que no haya sido verificado
        self.verified_prices = {
            FuelType.DIESEL: False,
            FuelType.DIESEL_PLUS: False,
            FuelType.GASOLINA: False
        }

    # Método que propone un precio para un tipo de gasolina
    def set_fuel_price(self, fuel_type, price):
        self.fuel_prices[fuel_type] = price

    # Método que verifica el precio de un tipo de gasolina
    def verify_fuel_price(self, fuel_type):
        self.verified_prices[fuel_type] = True

    # Método de clase que busca en la BD la gasolinera dado su identificador
    # y construye y devuelve un objeto de la clase FuelStation con los datos
    # obtenidos
    @classmethod
    def look_for_fuel_station_by_ID(cls, ID):
        # Buscar en la BD y construir el objeto fuel_station cuyo id es ID
        pass

# ────────────────────────────────────────────────────────────────────────────────
