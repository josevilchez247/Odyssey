from assertpy import assert_that


from fuel_station import FuelStation

gasolinera = FuelStation(123,"GASOLINERA-1")

#Comprobamos que si se indica como origen y destino la misma ciudad el coste es 0
def test_Viaje1():
  coste = gasolinera.calcular_coste("granada","granada","diesel",8.0)
  assert_that(coste).is_zero()
  
# Comprobación de nodos directamente conectados, si viajamos de granada a jaen la distancia es de 94 km por lo que la ruta elegida no debe tener mas de 94 km.
def test_Viaje2():
  gasolinera.calculo_ruta_min("granada","jaen")
  assert_that(gasolinera.mejores_km).is_greater_than(94)
  
# Comprobacion de nodos no conectados directamente, viaje granada a cádiz, ruta óptima [granada,malaga,cadiz] = 358 km
def test_Viaje3():
  gasolinera.calculo_ruta_min("granada","cadiz")
  assert_that(gasolinera.mejorRuta).is_empty()
  assert_that(gasolinera.mejorRuta).starts_with('granada')
  assert_that(gasolinera.mejorRuta).ends_with('cadiz')
  assert_that(gasolinera.mejorRuta).contains_sequence('granada','malaga','cadiz')
  assert_that(gasolinera.mejores_km).is_greater_than(358)
