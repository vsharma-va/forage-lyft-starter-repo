from engine1.capulet_engine import CapuletEngine
from engine1.sternman_engine import SternmanEngine
from engine1.willoughby_engine import WilloughbyEngine
from battery_types.nubbin_battery import NubbinBattery
from battery_types.spindler_battery import SpindlerBattery
from car import Car

from datetime import date

class CarFactory:
  @staticmethod
  def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
    engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
    battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
    return Car(engine, battery)
    
  @staticmethod
  def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
    engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
    battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
    return Car(engine, battery)
  
  @staticmethod
  def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
    engine = SternmanEngine(warning_light_is_on=warning_light_on)
    battery = SpindlerBattery(last_service_date=last_service_date, current_date=current_date)
    return Car(engine, battery)
    
  def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
    engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
    battery = NubbinBattery(last_service_date=last_service_date, current_date=current_date)
    return Car(engine, battery)
  
  @staticmethod  
  def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
    engine = CapuletEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
    battery = NubbinBattery(last_service_date=last_service_date, current_date=current_date)
    return Car(engine, battery)