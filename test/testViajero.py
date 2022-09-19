from assertpy import assert_that

def testViajeroData(viajeros):
  for viajero in viajeros: 
    assert_that(viajero).extracting('nombre').is_not_empty()
    assert_that(viajero).extracting('nombre').is_type_of(str)
    
    assert_that(viajero).extracting('clave').is_not_empty()
    assert_that(viajero).extracting('clave').is_length(8)
   
