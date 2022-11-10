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
from math import inf


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

        # Diccionario cuya clave es el tipo de gasolina y el valor es el precio oficial de la gasolina y el sugerido por los clientes en los comentarios
        # El argumento fuel_prices es un diccionario que almacena los precios 
        self.fuel_prices = {
            FuelType.DIESEL: [fuel_prices[FuelType.DIESEL],1.4],
            FuelType.DIESEL_PLUS: [fuel_prices[FuelType.DIESEL_PLUS],1.65],
            FuelType.GASOLINA: [fuel_prices[FuelType.GASOLINA],1.45]
        }
        
        self.mapa = [[0, 166, 0, 0, 0, 0, 0, 0],
        [166, 0, 94, 124, 0, 0, 0, 0],
        [0, 94, 0, 0, 108, 0, 0, 0],
        [0, 124, 0, 0, 158, 0, 234, 0],
        [0, 0, 108, 158, 0, 143, 0, 0],
        [0, 0, 0, 0, 143, 0, 120, 93],
        [0, 0, 0, 234, 0, 120, 0, 0],
        [0, 0, 0, 0, 0, 93, 0, 0]]

    # Método que cambia un precio oficial para un tipo de gasolina
    def set_fuel_price(self, fuel_type, price):
        self.fuel_prices[fuel_type][0] = price
        
    # Método que cambia un precio sugerido para un tipo de gasolina
    def set_fuel_price_suggested(self, fuel_type, price):
        self.fuel_prices[fuel_type][1] = price
    
    #Método que dada una ciudad de origen y una destino calcula la ruta mas corta y una estimación de coste.
    def calculo_ruta_min(self,origen,destino):
        n = len(self.mapa)

        dist = [inf]*n
        dist[origen] = mapa[origen][origen]  # 0

        visitadas = [False]*n
        parent = [-1]*n
        ruta = [{}]*n

        for count in range(n-1):
            mini = inf
            u = 0
            for v in range(len(visitadas)):#Selecciona el nodo que va a explorar viendo cual tiene menor peso
                if visitadas[v] == False and dist[v] <= mini:
                    mini = dist[v]
                    u = v
            visitadas[u] = True

            for v in range(n):
                if not(visitadas[v]) and self.mapa[u][v] != 0 and dist[u] + self.mapa[u][v] < dist[v]:
                    parent[v] = u
                    dist[v] = dist[u] + self.mapa[u][v]

        for i in range(n):
            j = i
            s = []
            while parent[j] != -1:
                s.append(j)
                j = parent[j]
            s.append(origen)
            ruta[i] = s[::-1]
            
         resul = []
         resul.append(dist[destino])
         resul.append(ruta[destino])
            
         return resul 

    
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
