import unittest
from datetime import datetime

from battery_types.nubbin_battery import NubbinBattery
from battery_types.spindler_battery import SpindlerBattery
from engine1.capulet_engine import CapuletEngine
from engine1.sternman_engine import SternmanEngine
from engine1.willoughby_engine import WilloughbyEngine
from tyres_types.octoprime_tyres import OctoprimeTyres
from tyres_types.carrigan_tyres import CarriganTyres


class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 25000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 50000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        indicator_on = True
        engine = SternmanEngine(indicator_on)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        indicator_on = False
        engine = SternmanEngine(indicator_on)
        self.assertFalse(engine.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        battery = SpindlerBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = SpindlerBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())


class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubbinBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = NubbinBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())
        
class TestOctoprimeTyres(unittest.TestCase):
    def test_tyres_should_be_serviced(self):
        tyre_wear_array = [0.9, 0.9, 0.9, 0.4]
        tyres = OctoprimeTyres(tyre_wear_array=tyre_wear_array)
        self.assertTrue(tyres.needs_service())
    
    def test_tyres_should_not_be_serviced(self):
        tyre_wear_array = [0.7, 0.5, 0.7, 0.6]
        tyres = OctoprimeTyres(tyre_wear_array=tyre_wear_array)
        self.assertFalse(tyres.needs_service())
        
class TestCarriganTyres(unittest.TestCase):
    def test_tyres_should_be_serviced(self):
        tyre_wear_array = [0.9, 0.8,0.8,0.8]
        tyres = CarriganTyres(tyre_wear_array=tyre_wear_array)
        self.assertTrue(tyres.needs_service())
        
    def test_tyres_should_not_be_serviced(self):
        tyre_wear_array = [0.8, 0.8, 0.8, 0.8]
        tyres = CarriganTyres(tyre_wear_array=tyre_wear_array)
        self.assertFalse(tyres.needs_service())


if __name__ == "__main__":
    unittest.main()
