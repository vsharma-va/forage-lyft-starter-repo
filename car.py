from abc import ABC, abstractmethod
from engine import Engine
from battery import Battery
from tyres import Tyres

class Car:
    def __init__(self, engine: Engine, battery: Battery, tyre: Tyres):
        self.engine = engine
        self.battery = battery
        self.tyre = tyre
        
    def needs_service(self) -> bool:
        if self.engine.needs_service() or self.battery.needs_service() or self.tyre.needs_service():
            return True
        else:
            return False