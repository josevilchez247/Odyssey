#
# ────────────────────────────────────────────────────────────────────
#   :::::: fuel_station.py : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────────────
#

# ─── PROYECT: Odyssey (https://github.com/josevilchez247/Odyssey) ───────────────
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

        # TODO estructurar los precios y verificados