from abc import ABC
from battery import Battery

class SpindlerBattery(Battery, ABC):
  def __init__(self, last_service_date, current_date):
    self.last_service_date = last_service_date
    self.current_date = current_date
  
  def needs_service(self) -> bool:
    if(self.last_service_date.replace(year=self.last_service_date+2) < self.current_date):
      return True
    else:
      return False