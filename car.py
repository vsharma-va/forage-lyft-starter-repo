from abc import ABC, abstractmethod
from engine import Engine
from battery import Battery

class Car:
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery
        
    def needs_service(self) -> bool:
        if self.engine.needs_service() or self.battery.needs_service():
            return True
        else:
            return False