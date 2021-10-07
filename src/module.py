#
# ────────────────────────────────────────────────────────────────────
#   :::::: module.py : :  :   :    :     :        :          :
# ────────────────────────────────────────────────────────────────────
#

# ─── PROYECT: Odyssey ───────────────────────────────────────────────────────────
# ─── OWNER: @josevilchez247 ─────────────────────────────────────────────────────
# ─── AUTHOR: @jantoniovr ────────────────────────────────────────────────────────
# ─── DATE: 7-10-2021 ────────────────────────────────────────────────────────────
# ─── VERSION: 1.0 ───────────────────────────────────────────────────────────────

from enumerators import *

# ────────────────────────────────────────────────────────────────────────────────

class Car:

    def __init__(self, fuelType, consume, tankCapacity, ownerDNI):
        self.fuelType       = fuelType
        self.consume        = consume
        self.tankCapacity   = tankCapacity
        self.fuelPercentage = 0
        self.ownerDNI       = ownerDNI

    def refuel(self, newFuelPercentage):
        self.fuelPercentage = newFuelPercentage

    def getOwner(self):
        # Buscar en la BD el viajero de DNI self.ownerDNI
        pass

    def spendFuel(self, spentFuel):
        # self.fuelPercentage -= ...
        pass

    # TODO Resto de métodos

# ────────────────────────────────────────────────────────────────────────────────

class FuelStation:

    def __init__(self, ID, name, location, fuelPrices):
        self.ID         = ID
        self.name       = name
        self.location   = location
        self.fuelPrices = {
            FuelType.DIESEL     : fuelPrices[FuelType.DIESEL],
            FuelType.DIESEL_PLUS: fuelPrices[FuelType.DIESEL_PLUS],
            FuelType.GASOLINA   : fuelPrices[FuelType.GASOLINA]
        }
        self.verifiedPrices = {
            FuelType.DIESEL     : False,
            FuelType.DIESEL_PLUS: False,
            FuelType.GASOLINA   : False
        }

    def setFuelPrice(self, fuelType, price):
        self.fuelPrices[fuelType] = price

    def verifyFuelPrice(self, fuelType):
        self.verifiedPrices[fuelType] = True
    
    @classmethod
    def getFuelStationByID(cls, ID):
        # Buscar en la BD y construir el objeto FuelStation cuyo id es ID
        pass
    
  # ────────────────────────────────────────────────────────────────────────────────

class Driver:
    
    def __init__(self):
        pass

    def __init__(self, DNI, name, email, phoneNumber, carID):
        self.DNI         = DNI
        self.name        = name
        self.email       = email
        self.phoneNumber = phoneNumber
        self.carID       = carID

    ## TODO getters y setters??

    def getCar(self):
        # Buscar en la BD el coche de matrícula self.carID
        pass

    def suggestPrice(IDFuelStation, fuelType, price):
        fuelStation = FuelStation.getFuelStationByID(IDFuelStation)
        fuelStation.setFuelPrice(fuelType, price)

    def verifyPrice(IDFuelStation, fuelType):
        fuelStation = FuelStation.getFuelStationByID(IDFuelStation)
        fuelStation.verifyFuelPrice(fuelType)