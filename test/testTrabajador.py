from assertpy import assert_that

def testTrabajadorData(trabajadores):
  
  for trabajador in trabajadores:
    
    assert_that(trabajador).extracting('id_fuel_station').is_not_none()
    assert_that(trabajador).extracting('id_fuel_station').is_type_of(int)
    assert_that(trabajador).extracting('id_fuel_station').is_greater_than_or_equal_to(1)
    assert_that(trabajador).extracting('id_fuel_station').is_less_than_or_equal_to(9999)
    
    assert_that(trabajador).extracting('nombre').is_not_empty()
    assert_that(trabajador).extracting('nombre').is_type_of(str)
    
    assert_that(trabajador).extracting('clave').is_not_empty()
    assert_that(trabajador).extracting('clave').is_length(8)
   
