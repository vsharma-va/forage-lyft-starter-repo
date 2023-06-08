from car_factory import CarFactory
from datetime import datetime
from serviceable import Serviceable

today = datetime.today().date()
last_service_date = today.replace(year=today.year - 3)
current_mileage = 100000
last_service_mileage = 100
new_car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage)
print(Serviceable.needs_service(new_car))

