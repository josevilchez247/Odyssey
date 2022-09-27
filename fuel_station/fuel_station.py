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

    def __init__(self, ID, name):
        self.ID = ID                    # Identificador único
        self.name = name                # Nombre de la gasolinera
        self.ciudades = ["granada","almeria","jaen","malaga","cadiz","cordoba","sevilla","huelva"]
        self.mejorRuta = []
        self.visitadas = []
        self.km_total = 0
        self.mejores_km = 99999999999999

        # Diccionario cuya clave es el tipo de gasolina y el valor es el precio oficial de la gasolina y el sugerido por los clientes en los comentarios
        # El argumento fuel_prices es un diccionario que almacena los precios 
        self.fuel_prices = {
            FuelType.DIESEL: [fuel_prices[FuelType.DIESEL],1.4],
            FuelType.DIESEL_PLUS: [fuel_prices[FuelType.DIESEL_PLUS],1.65],
            FuelType.GASOLINA: [fuel_prices[FuelType.GASOLINA],1.45]
        }
        
        #DICCIONARIO DE CONEXIONES ENTRE CIUDADES
        self.dc_rutas = {}
        for ciudad in self.ciudades:
            if ciudad not in self.dc.rutas: self.dc_rutas[ciudad] = {}
            if ciudad == "granada":
                self.dc_rutas[ciudad]["jaen"] = 94
                self.dc_rutas[ciudad]["malaga"] = 124
                self.dc_rutas[ciudad]["almeria"] = 166
            elif ciudad == "almeria":
                self.dc_rutas[ciudad]["granada"] = 166
            elif ciudad == "jaen":
                self.dc_rutas[ciudad]["granada"] = 94
                self.dc_rutas[ciudad]["cordoba"] = 108
            elif ciudad == "malaga":
                self.dc_rutas[ciudad]["granada"] = 124
                self.dc_rutas[ciudad]["cordoba"] = 158
                self.dc_rutas[ciudad]["cadiz"] = 234
            elif ciudad == "cordoba":
                self.dc_rutas[ciudad]["jaen"] = 108
                self.dc_rutas[ciudad]["sevilla"] = 143
                self.dc_rutas[ciudad]["malaga"] = 158
            elif ciudad == "sevilla":
                self.dc_rutas[ciudad]["huelva"] = 93
                self.dc_rutas[ciudad]["cadiz"] = 120
                self.dc_rutas[ciudad]["cordoba"] = 143
            elif ciudad == "cadiz":
                self.dc_rutas[ciudad]["sevilla"] = 120
                self.dc_rutas[ciudad]["malaga"] = 234
            elif ciudad == "huelva":
                self.dc_rutas[ciudad]["sevilla"] = 93

    # Método que cambia un precio oficial para un tipo de gasolina
    def set_fuel_price(self, fuel_type, price):
        self.fuel_prices[fuel_type][0] = price
        
    # Método que cambia un precio sugerido para un tipo de gasolina
    def set_fuel_price_suggested(self, fuel_type, price):
        self.fuel_prices[fuel_type][1] = price
        
    def obtener_km_ruta(ruta):
        origen = ruta[0]
        km = 0
        ruta.remove(origen)
        for ciudad in ruta:
            km += self.dc_rutas[origen][ciudad]
            origen = ciudad
            
        return km
    
    #Método que dada una ciudad de origen y una destino calcula la ruta mas corta y una estimación de coste.
    def calculo_ruta_min(self,origen,destino):

        if origen not in self.visitadas:self.visitadas.append(origen)
           
        if destino in self.dc_rutas[origen]: #Comprobamos si el destino tiene conexion directa con el origen
            self.visitadas.append(destino)
            km_ruta = obtener_km_ruta(self.visitadas)
            if km_ruta < self.mejores_km: 
                self.mejorRuta = self.visitadas
                self.mejores_km = km_ruta
  
            self.visitadas.remove(destino)

        else:
            for clave_d in self.dc_rutas[origen]:

                if clave_d in self.visitadas:continue    
                calculo_ruta(self,clave_d,destino)

        self.visitadas.remove(origen)
        return 0
    
    #Introducimos el origen, destino del viaje, el tipo de combustible y el consumo medio del vehículo
    def calcular_coste(self,origen,destino,fuel_type,consumo_medio):
        calculo_ruta_min(self,origen,destino)
        litros = self.mejores_km/consumo_medio
        coste = litro * self.fuel_prices[fuel_type][1]
        return coste

    # Método de clase que busca en la BD la gasolinera dado su identificador
    # y construye y devuelve un objeto de la clase FuelStation con los datos
    # obtenidos
    @classmethod
    def look_for_fuel_station_by_ID(cls, ID):
        # Buscar en la BD y construir el objeto fuel_station cuyo id es ID
        pass

# ────────────────────────────────────────────────────────────────────────────────
