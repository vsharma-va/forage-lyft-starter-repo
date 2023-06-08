from car import Car

class Serviceable:
  @staticmethod
  def needs_service(car: Car):
    return car.needs_service()